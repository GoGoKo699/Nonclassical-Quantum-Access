#!/usr/bin/env python3
"""Verify the canonical one-parameter five-cycle quantum access construction.

The default command verifies exact parameter identities using only the Python
standard library. Add --numerical to reconstruct the full dimension-eight
encoding and every one of its five erasure/recovery channels with NumPy.

Examples, run from the repository root:
    python verification/verify_family.py
    python -S verification/verify_family.py
    OPENBLAS_NUM_THREADS=1 python verification/verify_family.py --numerical
    python verification/verify_family.py --numerical --case optimal
    python verification/verify_family.py --numerical --case rational
    python verification/verify_family.py --numerical --x 0.1 --orientation -1

All output is JSON on stdout. Redirect stdout to save a report. No optimizer,
saved numerical vector, or implementation from verify_exact.py is used here.
The canonical construction has no site-dependent phase: both source states
are cyclically invariant, and every ordered adjacent pair uses the same
decoder. The parameter domain is 0 <= x <= 3/4.

Exact parameter identities and floating-point channel diagnostics are reported
separately. The latter corroborate the mathematical construction; a small
floating-point residual is not a proof of an exact channel identity. The
separate verify_exact.py supplies a complete exact channel certificate for
the rational member x=1/8.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math
import platform
from typing import Any


class Polynomial:
    """Univariate polynomials with exact rational coefficients."""

    def __init__(self, coefficients: int | dict[int, Fraction | int] = 0):
        if isinstance(coefficients, int):
            coefficients = {0: coefficients}
        self.coefficients = {
            degree: Fraction(coefficient)
            for degree, coefficient in coefficients.items() if coefficient
        }

    def __add__(self, other: int | Polynomial) -> Polynomial:
        if isinstance(other, int):
            other = Polynomial(other)
        coefficients = self.coefficients.copy()
        for degree, coefficient in other.coefficients.items():
            coefficients[degree] = coefficients.get(degree, 0) + coefficient
        return Polynomial(coefficients)

    __radd__ = __add__

    def __neg__(self) -> Polynomial:
        return Polynomial({degree: -coefficient
                           for degree, coefficient in self.coefficients.items()})

    def __sub__(self, other: int | Polynomial) -> Polynomial:
        return self + (-other if isinstance(other, Polynomial) else -other)

    def __rsub__(self, other: int | Polynomial) -> Polynomial:
        return -self + other

    def __mul__(self, other: int | Polynomial) -> Polynomial:
        if isinstance(other, int):
            other = Polynomial(other)
        coefficients: dict[int, Fraction] = {}
        for i, a in self.coefficients.items():
            for j, b in other.coefficients.items():
                coefficients[i + j] = coefficients.get(i + j, Fraction(0)) + a * b
        return Polynomial(coefficients)

    __rmul__ = __mul__

    def __pow__(self, power: int) -> Polynomial:
        if power < 0:
            raise ValueError("A polynomial power must be nonnegative.")
        result = Polynomial(1)
        for _ in range(power):
            result = result * self
        return result

    def is_zero(self) -> bool:
        return not self.coefficients


@dataclass(frozen=True)
class Qsqrt3:
    """Exact a+b*sqrt(3), including exact ordering against zero."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    @staticmethod
    def lift(value: int | Fraction | Qsqrt3) -> Qsqrt3:
        return value if isinstance(value, Qsqrt3) else Qsqrt3(Fraction(value))

    def __add__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        other = self.lift(other)
        return Qsqrt3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> Qsqrt3:
        return Qsqrt3(-self.a, -self.b)

    def __sub__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self + -self.lift(other)

    def __rsub__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self.lift(other) + -self

    def __mul__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        other = self.lift(other)
        return Qsqrt3(self.a * other.a + 3 * self.b * other.b,
                      self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def reciprocal(self) -> Qsqrt3:
        norm = self.a * self.a - 3 * self.b * self.b
        if not norm:
            raise ZeroDivisionError
        return Qsqrt3(self.a / norm, -self.b / norm)

    def __truediv__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self * self.lift(other).reciprocal()

    def __rtruediv__(self, other: int | Fraction | Qsqrt3) -> Qsqrt3:
        return self.lift(other) * self.reciprocal()

    def __pow__(self, power: int) -> Qsqrt3:
        if power < 0:
            return self.reciprocal() ** -power
        result = Qsqrt3(1)
        for _ in range(power):
            result = result * self
        return result

    def positive(self) -> bool:
        if not self.b:
            return self.a > 0
        if not self.a:
            return self.b > 0
        if self.a > 0 and self.b > 0:
            return True
        if self.a < 0 and self.b < 0:
            return False
        if self.a > 0:
            return self.a * self.a > 3 * self.b * self.b
        return 3 * self.b * self.b > self.a * self.a


def require(condition: bool, message: str) -> None:
    """Keep verification active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def verify_exact_parameters() -> dict[str, Any]:
    """Prove the normalization, advantage interval, and family optimum algebra."""
    x = Polynomial({1: 1})
    y = 1 - x
    b1_numerator = 2 * (2 * x - 1) ** 2
    b2_numerator = Polynomial(2)
    gamma_numerator = y - (2 * x - 1) ** 2
    d_numerator = 4 * y + b1_numerator + b2_numerator + gamma_numerator
    checks = {
        "gamma_squared": gamma_numerator - x * (3 - 4 * x),
        "decoder_row_normalization":
            b1_numerator + 2 * gamma_numerator - 2 * y,
        "source_denominator": d_numerator - ((5 - 4 * x) * y + 3),
        "denominator_in_y": d_numerator - (y + 4 * y ** 2 + 3),
        "advantage_factorization": d_numerator - 8 * y - x * (4 * x - 1),
    }
    for name, polynomial in checks.items():
        require(polynomial.is_zero(), f"Exact polynomial identity failed: {name}")

    # Coefficient convolution proves
    # y*(D-(1+4*sqrt(3))) = (2*y-sqrt(3))**2, identically in y.
    r = Qsqrt3(0, 1)
    linear = [-r, Qsqrt3(2)]
    square = [Qsqrt3(0) for _ in range(3)]
    for i, left in enumerate(linear):
        for j, right in enumerate(linear):
            square[i + j] += left * right
    difference = [Qsqrt3(3), Qsqrt3(1), Qsqrt3(4)]
    difference[1] -= 1 + 4 * r
    require(difference == square, "Exact family optimality factorization failed")

    x_star = 1 - r / 2
    b1 = 2 * (2 * x_star - 1) ** 2 / (1 - x_star)
    b2 = 2 / (1 - x_star)
    gamma2 = 1 - b1 / 2
    denominator = 4 + b1 + b2 + gamma2
    optimum_checks = {
        "optimal_parameter_in_advantage_interval":
            x_star.positive() and (Fraction(1, 4) - x_star).positive(),
        "optimal_beta1_norm": b1 == 16 / r - 8,
        "optimal_beta2_norm": b2 == 4 / r,
        "optimal_gamma_squared": gamma2 == 5 - 8 / r and gamma2.positive(),
        "optimal_denominator": denominator == 1 + 4 * r,
        "strict_advantage": (16 / denominator - 2).positive(),
    }
    for name, condition in optimum_checks.items():
        require(condition, f"Exact algebraic comparison failed: {name}")

    xr = Fraction(1, 8)
    rb1 = 2 * (2 * xr - 1) ** 2 / (1 - xr)
    rb2 = 2 / (1 - xr)
    rgamma = 1 - rb1 / 2
    rd = 4 + rb1 + rb2 + rgamma
    require((rb1, rb2, rgamma, rd) == (
        Fraction(9, 7), Fraction(16, 7), Fraction(5, 14), Fraction(111, 14)
    ), "Exact rational-member normalization failed")
    require(16 / rd == Fraction(224, 111), "Exact rational success sum failed")
    require(16 / (5 * rd) == Fraction(224, 555), "Exact rational pair success failed")

    return {
        "scope": "Parameter identities only; the exact full-channel certificate is verify_exact.py.",
        "arithmetic": ["rational polynomial coefficients", "Q(sqrt(3))", "rational comparisons"],
        "parameter_domain": "0 <= x <= 3/4",
        "polynomial_identities": list(checks),
        "optimum_identity": "D-(1+4*sqrt(3))=(2*y-sqrt(3))^2/y, y=1-x>0",
        "optimal_parameter": "x=1-sqrt(3)/2",
        "optimal_denominator": "1+4*sqrt(3)",
        "optimal_success_per_pair": "16/(5*(1+4*sqrt(3)))",
        "optimal_success_sum": "16/(1+4*sqrt(3))",
        "optimality_scope": "This one-parameter construction, not arbitrary quantum encoders.",
        "strict_advantage_interval": "0 < x < 1/4",
        "algebraic_checks": list(optimum_checks),
        "rational_member": {
            "x": "1/8", "denominator": "111/14",
            "success_per_pair": "224/555", "success_sum": "224/111",
        },
        "status": "PASS",
    }


@dataclass(frozen=True)
class Parameters:
    x: float
    orientation: int
    t: complex
    beta1: complex
    beta2: complex
    gamma: float
    denominator: float
    success: float


def parameters(x: float, orientation: int = 1) -> Parameters:
    if not math.isfinite(x) or not 0 <= x <= 0.75:
        raise ValueError("The canonical family requires 0 <= x <= 3/4.")
    if orientation not in (-1, 1):
        raise ValueError("The phase orientation must be +1 or -1.")
    t = complex(x, orientation * math.sqrt(1 - x * x))
    beta2 = 2 * t * t / (1 - t)
    beta1 = 2 * t + t * beta2
    gamma = math.sqrt(x * (3 - 4 * x) / (1 - x))
    # This is the independently derived closed form; the channel audit checks
    # it against norms of the explicit source vectors below.
    denominator = 5 - 4 * x + 3 / (1 - x)
    return Parameters(x, orientation, t, beta1, beta2, gamma,
                      denominator, 16 / (5 * denominator))


def source_states(p: Parameters):
    """Construct f and g with local computational order (v,0,1,2)."""
    import numpy as np

    defect, zero, one, two = range(4)
    f = np.zeros(4 ** 5, dtype=np.complex128)
    g = np.zeros_like(f)
    for j in range(5):
        for offset in range(1, 5):
            word = [one] * 5
            word[j], word[(j + offset) % 5] = defect, zero
            f[np.ravel_multi_index(word, (4,) * 5)] += p.t ** (offset - 1)
        for gap, amplitude in ((1, p.beta1), (2, p.beta2)):
            word = [one] * 5
            word[j] = word[(j + gap) % 5] = zero
            g[np.ravel_multi_index(word, (4,) * 5)] += amplitude
        word = [one] * 5
        word[j] = two
        g[np.ravel_multi_index(word, (4,) * 5)] += p.gamma
    return f, g


def pair_kraus(p: Parameters):
    """K[base Kraus label, output qubit, ordered ququart pair]."""
    import numpy as np

    defect, zero, one, two = range(4)
    K = np.zeros((2, 2, 16), dtype=np.complex128)
    s = math.sqrt(2)
    K[0, 0, 4 * defect + zero] = 1 / s
    K[0, 0, 4 * zero + defect] = p.t ** -3 / s
    K[1, 0, 4 * defect + one] = 1 / s
    K[1, 0, 4 * one + defect] = p.t / s
    K[0, 1, 4 * zero + zero] = p.beta1.conjugate() / s
    K[0, 1, 4 * one + two] = p.gamma / s
    K[0, 1, 4 * two + one] = p.gamma / s
    K[1, 1, 4 * zero + one] = -p.t / s
    K[1, 1, 4 * one + zero] = 1 / s
    return K


def encoding_isometry(p: Parameters, f, g):
    """Physical V: C^2 -> (C^8)^tensor5; local index = ququart + 4*flag."""
    import numpy as np

    words = np.indices((4,) * 5).reshape(5, -1)
    indices0 = np.ravel_multi_index(words, (8,) * 5)
    indices1 = np.ravel_multi_index(words + 4, (8,) * 5)
    V = np.zeros((8 ** 5, 2), dtype=np.complex128)
    scale = math.sqrt(5 * p.denominator)
    V[indices0, 0], V[indices1, 0] = f / scale, g / scale
    V[indices0, 1], V[indices1, 1] = g / scale, f / scale
    return V


def flagged_pair_kraus(K):
    """Four success operators on a dimension-eight pair; flag 1 corrects with X."""
    import numpy as np

    X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    L = np.zeros((4, 2, 64), dtype=np.complex128)
    for flag in (0, 1):
        corrected = K if flag == 0 else np.einsum("ab,lbc->lac", X, K)
        for b0 in range(4):
            for b1 in range(4):
                physical_column = 8 * (b0 + 4 * flag) + b1 + 4 * flag
                L[2 * flag:2 * flag + 2, :, physical_column] = corrected[:, :, 4 * b0 + b1]
    return L


def verify_numerical_channel(p: Parameters, name: str,
                             tolerance: float = 3e-11) -> dict[str, Any]:
    """Independently contract all physical erasure/recovery channels with NumPy."""
    import numpy as np

    f, g = source_states(p)
    V = encoding_isometry(p, f, g)
    K = pair_kraus(p)
    L = flagged_pair_kraus(K)
    identity = np.eye(2, dtype=np.complex128)
    bell = np.array([1, 0, 0, 1], dtype=np.complex128) / math.sqrt(2)
    bell_projector = np.outer(bell, bell.conjugate())
    norm_f, norm_g = float(np.vdot(f, f).real), float(np.vdot(g, g).real)
    rotation = lambda a: a.reshape((4,) * 5).transpose(4, 0, 1, 2, 3).reshape(-1)
    residuals = {
        "source_f_norm": abs(norm_f - 20),
        "source_g_norm": abs(norm_g - 5 * (p.denominator - 4)),
        "source_orthogonality": float(abs(np.vdot(f, g))),
        "cyclic_invariance": float(max(np.linalg.norm(rotation(f) - f),
                                        np.linalg.norm(rotation(g) - g))),
        "encoding_isometry": float(np.linalg.norm(V.conjugate().T @ V - identity)),
        "decoder_contraction_excess": max(0.0, float(np.linalg.eigvalsh(
            K.reshape(4, 16) @ K.reshape(4, 16).conjugate().T)[-1] - 1)),
        "flagged_decoder_contraction_excess": max(0.0, float(np.linalg.eigvalsh(
            L.reshape(8, 64) @ L.reshape(8, 64).conjugate().T)[-1] - 1)),
    }
    pair_reports = []
    for i in range(5):
        pair = [i, (i + 1) % 5]
        erased = [j for j in range(5) if j not in pair]
        W = V.reshape((8,) * 5 + (2,)).transpose(
            pair + erased + [5]
        ).reshape(64, 512, 2)

        # E[label, output, erased basis state, logical input] is the complete
        # effective Kraus family after encoding, erasure, and physical recovery.
        E = np.einsum("lab,bek->laek", L, W)
        scalar = (E[:, 0, :, 0] + E[:, 1, :, 1]) / 2
        scalar_identity = np.einsum("ak,le->laek", identity, scalar)
        effective_kraus_error = float(np.linalg.norm(E - scalar_identity))
        observed_success = float(np.vdot(scalar, scalar).real)
        vectorized = E.transpose(3, 1, 0, 2).reshape(4, -1) / math.sqrt(2)
        choi = vectorized @ vectorized.conjugate().T
        success_effect = np.einsum("laej,laek->jk", E.conjugate(), E)
        pair_residuals = {
            "effective_kraus_scalar_identity": effective_kraus_error,
            "normalized_choi": float(np.linalg.norm(choi - p.success * bell_projector)),
            "success_input_independence": float(np.linalg.norm(success_effect - p.success * identity)),
            "probability_formula": abs(observed_success - p.success),
        }
        count = int(np.count_nonzero(np.abs(scalar) > 1e-12))
        require(count == 8, f"Unexpected effective Kraus support for {name}, pair {pair}: {count}")
        pair_reports.append({
            "ordered_pair": pair,
            "success_probability": observed_success,
            "nonzero_effective_kraus": count,
            "residuals": pair_residuals,
        })

    maximum = max(list(residuals.values()) + [
        value for pair in pair_reports for value in pair["residuals"].values()
    ])
    require(math.isfinite(maximum) and maximum < tolerance,
            f"Floating channel diagnostic failed for {name}: {maximum:g} >= {tolerance:g}")
    return {
        "case": name,
        "x": p.x,
        "phase_orientation": p.orientation,
        "local_dimension": 8,
        "encoder_shape": list(V.shape),
        "source_support_sizes": [int(np.count_nonzero(np.abs(f) > 1e-12)),
                                 int(np.count_nonzero(np.abs(g) > 1e-12))],
        "source_norms_squared": [norm_f, norm_g],
        "denominator_formula": p.denominator,
        "success_per_pair_formula": p.success,
        "success_sum_formula": 5 * p.success,
        "success_sum_observed": sum(pair["success_probability"] for pair in pair_reports),
        "residuals": residuals,
        "maximum_residual": maximum,
        "absolute_residual_tolerance": tolerance,
        "pairs": pair_reports,
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--numerical", action="store_true",
                        help="Additionally reconstruct all five physical channels with NumPy.")
    parser.add_argument("--case", action="append",
                        choices=("optimal", "rational", "boundaries", "conjugate"),
                        help="Select a numerical case group; repeat to combine. Default: all groups.")
    parser.add_argument("--x", type=float,
                        help="Add a numerical member with 0 <= x <= 3/4; without --case, run only this member.")
    parser.add_argument("--orientation", type=int, choices=(-1, 1), default=1,
                        help="Sign of Im(t) for a custom --x (default: +1).")
    args = parser.parse_args()
    if (args.case or args.x is not None) and not args.numerical:
        parser.error("--case and --x require --numerical")
    if args.orientation != 1 and args.x is None:
        parser.error("--orientation applies to --x; use --case conjugate for the conjugate optimum")
    if args.x is not None and (not math.isfinite(args.x) or not 0 <= args.x <= 0.75):
        parser.error("--x must satisfy 0 <= x <= 3/4")

    report: dict[str, Any] = {
        "verifier": "canonical_five_cycle_parameter_family",
        "schema_version": 1,
        "runtime": {"python": platform.python_version()},
        "exact_parameter_identities": verify_exact_parameters(),
        "floating_channel_diagnostics": {"enabled": False},
    }
    if args.numerical:
        try:
            import numpy as np
        except ImportError:
            parser.error("Numerical mode requires NumPy; install verification/requirements.txt.")
        report["runtime"]["numpy"] = np.__version__
        x_star = 1 - math.sqrt(3) / 2
        groups = {
            "optimal": [("optimal", x_star, 1)],
            "rational": [("rational_x_1_over_8", 0.125, 1)],
            "boundaries": [("domain_boundary_x_0", 0.0, 1),
                           ("advantage_boundary_x_1_over_4", 0.25, 1),
                           ("domain_boundary_x_3_over_4", 0.75, 1)],
            "conjugate": [("conjugate_optimal", x_star, -1)],
        }
        selected_groups = args.case if args.case else ([] if args.x is not None else list(groups))
        cases = []
        for group in dict.fromkeys(selected_groups):
            cases.extend(groups[group])
        if args.x is not None:
            cases.append(("custom", args.x, args.orientation))
        report["floating_channel_diagnostics"] = {
            "enabled": True,
            "scope": "Numerical corroboration of full channels; not an exact arithmetic certificate.",
            "dtype": "complex128",
            "matrix_residual_norm": "Frobenius",
            "construction": "Canonical cyclically invariant family, with no site-dependent phase.",
            "cases": [verify_numerical_channel(parameters(x, sign), name)
                      for name, x, sign in cases],
        }
    report["status"] = "PASS"
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
