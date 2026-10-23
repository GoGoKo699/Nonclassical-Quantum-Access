#!/usr/bin/env python3
"""Exact sparse-channel certificate for the x=1/8 pentagon code.

Only Python's standard library is used. Amplitudes are evaluated in
Q(u,v), u^2=-7, v^2=5/14, with u=i*sqrt(7) and v positive real.
The source normalization and the common decoder factor 1/sqrt(2)
are kept outside the field. No floating-point tolerance is used.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

if not __debug__:
    raise RuntimeError("Exact verification requires assertions; run Python without -O or -OO.")


@dataclass(frozen=True)
class Scalar:
    """Coefficients of 1, u, v, uv, in that order."""

    c: tuple[F, F, F, F]

    @staticmethod
    def lift(value):
        if isinstance(value, Scalar):
            return value
        return Scalar((F(value), F(0), F(0), F(0)))

    def __add__(self, other):
        other = Scalar.lift(other)
        return Scalar(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Scalar(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self + (-Scalar.lift(other))

    def __rsub__(self, other):
        return Scalar.lift(other) - self

    def __mul__(self, other):
        other = Scalar.lift(other)
        result = [F(0)] * 4
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                factor = F(1)
                if i & j & 1:
                    factor *= -7
                if i & j & 2:
                    factor *= F(5, 14)
                result[i ^ j] += factor * a * b
        return Scalar(tuple(result))

    __rmul__ = __mul__

    def __truediv__(self, denominator):
        if isinstance(denominator, Scalar):
            raise TypeError("Only rational scalar division is needed.")
        return self * (1 / F(denominator))

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("Use conjugation for the inverse unit phase.")
        result = ONE_SCALAR
        base = self
        while power:
            if power & 1:
                result *= base
            base *= base
            power //= 2
        return result

    def conjugate(self):
        return Scalar((self.c[0], -self.c[1], self.c[2], -self.c[3]))

    def rational(self):
        assert self.c[1:] == (F(0), F(0), F(0)), self.c
        return self.c[0]

    def norm_squared(self):
        return (self.conjugate() * self).rational()

    def __bool__(self):
        return any(self.c)


ZERO_SCALAR = Scalar.lift(0)
ONE_SCALAR = Scalar.lift(1)
U = Scalar((F(0), F(1), F(0), F(0)))
GAMMA = Scalar((F(0), F(0), F(1), F(0)))
T = (1 + 3 * U) / 8
BETA2 = -(35 + 9 * U) / 28
BETA1 = -3 * BETA2 / 4
D = F(111, 14)
SOURCE_NORM = 5 * D
DEFECT, BG_ZERO, BG_ONE, BG_TWO = range(4)
PAIRS = [(i, (i + 1) % 5) for i in range(5)]


def add_amplitude(state, basis, amplitude):
    state[basis] = state.get(basis, ZERO_SCALAR) + amplitude
    if not state[basis]:
        del state[basis]


def source_states():
    f, g = {}, {}
    for j in range(5):
        for offset in range(1, 5):
            basis = [BG_ONE] * 5
            basis[j] = DEFECT
            basis[(j + offset) % 5] = BG_ZERO
            add_amplitude(f, tuple(basis), T ** (offset - 1))
        for offset, coefficient in [(1, BETA1), (2, BETA2)]:
            basis = [BG_ONE] * 5
            basis[j] = basis[(j + offset) % 5] = BG_ZERO
            add_amplitude(g, tuple(basis), coefficient)
        basis = [BG_ONE] * 5
        basis[j] = BG_TWO
        add_amplitude(g, tuple(basis), GAMMA)
    assert len(f) == 20 and len(g) == 15
    assert not set(f).intersection(g)
    return f, g


def inner(left, right):
    return sum((a.conjugate() * right.get(k, ZERO_SCALAR)
                for k, a in left.items()), ZERO_SCALAR)


def decoder_rows():
    """Rows of L_ell=sqrt(2) K_ell, indexed by (ell, logical output)."""
    return {
        (0, 0): {(DEFECT, BG_ZERO): ONE_SCALAR,
                 (BG_ZERO, DEFECT): T.conjugate() ** 3},
        (0, 1): {(BG_ZERO, BG_ZERO): BETA1.conjugate(),
                 (BG_ONE, BG_TWO): GAMMA, (BG_TWO, BG_ONE): GAMMA},
        (1, 0): {(DEFECT, BG_ONE): ONE_SCALAR,
                 (BG_ONE, DEFECT): T},
        (1, 1): {(BG_ZERO, BG_ONE): -T,
                 (BG_ONE, BG_ZERO): ONE_SCALAR},
    }


def flagged_columns(f, g):
    """Unnormalized columns of V; each carries the factor 1/sqrt(5D)."""
    columns = []
    for logical in range(2):
        column = {}
        for flag in range(2):
            source = (f, g)[logical ^ flag]
            for basis, amplitude in source.items():
                # A local carrier is (ququart level, flag bit).
                add_amplitude(column, tuple((b, flag) for b in basis), amplitude)
        columns.append(column)
    return columns


def effective_kraus(columns, rows, pair):
    """Contract all erased basis states and all successful recovery labels.

    Returned matrices omit the common factor 1/sqrt(2*5D). The key includes
    the measured local flag, the decoder Kraus label, and the complete
    erased-carrier basis string. Zero matrices are removed only after all
    coherent amplitudes have been combined.
    """
    environment_sites = [j for j in range(5) if j not in pair]
    matrices = {}
    for logical, column in enumerate(columns):
        for basis, amplitude in column.items():
            left, right = basis[pair[0]], basis[pair[1]]
            assert left[1] == right[1]
            flag = left[1]
            pair_basis = (left[0], right[0])
            environment = tuple(basis[j] for j in environment_sites)
            for (ell, output), row in rows.items():
                coefficient = row.get(pair_basis, ZERO_SCALAR)
                if coefficient:
                    key = (flag, ell, environment)
                    matrix = matrices.setdefault(key, [[ZERO_SCALAR] * 2
                                                       for _ in range(2)])
                    # Conditional X is applied after the pair decoder.
                    matrix[output ^ flag][logical] += coefficient * amplitude
    return {k: m for k, m in matrices.items()
            if any(value for row in m for value in row)}


def apply_success_projector(state, rows, pair):
    """Apply P=sum K_ell^dagger K_ell=(sum L_ell^dagger L_ell)/2."""
    result = {}
    for basis, amplitude in state.items():
        old = (basis[pair[0]], basis[pair[1]])
        for row in rows.values():
            coefficient = row.get(old, ZERO_SCALAR)
            if not coefficient:
                continue
            for new, new_coefficient in row.items():
                updated = list(basis)
                updated[pair[0]], updated[pair[1]] = new
                add_amplitude(result, tuple(updated),
                              amplitude * coefficient * new_coefficient.conjugate() / 2)
    return result


def verify():
    assert U * U == Scalar.lift(-7)
    assert GAMMA * GAMMA == Scalar.lift(F(5, 14))
    assert T.norm_squared() == 1
    assert BETA1 == -3 * BETA2 / 4
    assert (1 - T) * BETA2 == 2 * T ** 2
    assert BETA1 - T * BETA2 == 2 * T
    assert BETA2 - T * BETA1 == 2 * T ** 3
    assert BETA1.norm_squared() == F(9, 7)
    assert BETA2.norm_squared() == F(16, 7)
    assert BETA1.norm_squared() / 2 + GAMMA.norm_squared() == 1

    f, g = source_states()
    assert inner(f, f).rational() == 20
    assert inner(g, g).rational() == F(275, 14)
    assert inner(f, g) == ZERO_SCALAR
    for state in (f, g):
        rotated = {basis[-1:] + basis[:-1]: value for basis, value in state.items()}
        assert rotated == state

    rows = decoder_rows()
    for label, row in rows.items():
        for other_label, other_row in rows.items():
            target = 2 if label == other_label else 0
            assert inner(row, other_row) == Scalar.lift(target)
    # Therefore the stacked K rows are orthonormal and K^dagger K is a
    # projector. This proves trace nonincrease on the entire pair space.

    columns = flagged_columns(f, g)
    for i in range(2):
        for j in range(2):
            target = SOURCE_NORM if i == j else 0
            assert inner(columns[i], columns[j]) == Scalar.lift(target)

    pair_results = []
    for pair in PAIRS:
        matrices = effective_kraus(columns, rows, pair)
        assert len(matrices) == 8
        total_norm = F(0)
        for matrix in matrices.values():
            assert matrix[0][1] == matrix[1][0] == ZERO_SCALAR
            assert matrix[0][0] == matrix[1][1]
            assert matrix[0][0].norm_squared() == 4
            total_norm += matrix[0][0].norm_squared()
        probability = total_norm / (2 * SOURCE_NORM)
        assert probability == F(224, 555)
        pair_results.append({"pair": list(pair), "nonzero_effective_kraus": 8,
                             "success_probability": str(probability),
                             "logical_channel": "p * identity, exactly"})

    disjoint = [(i, j) for i in range(5) for j in range(i + 1, 5)
                if set(PAIRS[i]).isdisjoint(PAIRS[j])]
    assert len(disjoint) == 5
    for i, j in disjoint:
        for source in (f, g):
            assert not apply_success_projector(
                apply_success_projector(source, rows, PAIRS[j]), rows, PAIRS[i])

    independent_profiles = []
    for bits in range(32):
        authorized = [i for i in range(5) if bits & (1 << i)]
        if all(not (i in authorized and j in authorized) for i, j in disjoint):
            independent_profiles.append(authorized)
    assert len(independent_profiles) == 11
    assert max(map(len, independent_profiles)) == 2

    # Exact proof that the family optimum D*=1+4sqrt(3) lies below 8:
    # 4sqrt(3)<7 follows from 48<49. The AM-GM argument is in the text.
    assert 16 * 3 < 7 * 7
    total = 5 * F(224, 555)
    assert total - 2 == F(2, 111)
    return {
        "status": "PASS",
        "arithmetic": "Fractions in Q(u,v), u^2=-7, v^2=5/14; no tolerances",
        "family_parameter_x": "1/8",
        "physical_carriers": 5,
        "dimension_per_carrier": 8,
        "logical_dimension": 2,
        "source_terms": {"f": len(f), "g": len(g)},
        "source_norm_squared": str(SOURCE_NORM),
        "decoder_row_gram": "2 * I_4 for L=sqrt(2)K, exactly",
        "encoder_gram": "I_2 after normalization, exactly",
        "pair_channels": pair_results,
        "joint_success_on_disjoint_pairs": "zero on both codewords, exactly",
        "disjoint_pair_contexts": [list(p) for p in disjoint],
        "deterministic_binary_profiles": len(independent_profiles),
        "deterministic_success_sum_max": 2,
        "success_sum": str(total),
        "advantage_in_sum": "2/111",
        "average_success": "224/555",
        "advantage_in_average": "2/555",
        "scope": "Exact finite construction and binary-profile enumeration; general minimality and family optimization use the written proofs and cited results.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the deterministic JSON certificate.")
    parser.add_argument("--check", type=Path, help="Compare with a committed JSON certificate.")
    args = parser.parse_args()
    report = verify()
    if args.check:
        assert json.loads(args.check.read_text()) == report, "Expected certificate differs."
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
