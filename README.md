# Nonclassical Quantum Access

Can exact recovery probabilities always be explained by a classical lottery over deterministic quantum access patterns?

This repository gives an explicit negative answer. One unknown qubit is encoded isometrically into five dimension-eight carriers arranged on a cycle. If any adjacent pair survives and the other three carriers are erased, a joint decoder recovers the qubit exactly with probability

```math
\boxed{
p=\frac{16}{5(1+4\sqrt3)}
=0.403622347593226\ldots .
}
```

The same decoder works for every ordered adjacent pair. For a uniformly chosen adjacent pair, every input-independent mixture of binary exact-access protocols has average success at most $`2/5`$. The benchmark permits arbitrary quantum encodings and arbitrary finite carrier dimensions.

The improvement is a strict separation of recovery profiles. Five carriers are minimal in this model, by combining the construction with the established classification for four or fewer carriers. Here a carrier is a complete dimension-eight block, not an individual physical qubit.

## Principal results

| Result | Statement | Proof |
|---|---|---|
| Exact heralded recovery | Every accepted logical output equals the input, including its entanglement with an external reference | [Model](science/model.md), [recovery](science/recovery.md) |
| Uniform five-pair score | $`Q=\sum_iq_i=16/(1+4\sqrt3)>2`$ | [Construction](science/construction.md), [parameter family](science/parameter_family.md) |
| Deterministic-mixture benchmark | $`Q\le2`$ for every mixture of binary quantum-access profiles, without restricting carrier dimensions | [Access profiles](science/access_profiles.md) |
| Smallest carrier number | No such separation exists on four or fewer carriers in the unrestricted finite-dimension model | [Minimality proof and attribution](science/access_profiles.md#five-carrier-minimality) |
| Exact arithmetic example | At $`x=1/8`$, every pair has $`q_i=224/555`$ and $`Q=224/111`$ | [Certificate](verification/expected/exact_certificate.json) |
| Full attainable family | The displayed family has strict advantage exactly for $`0<x<1/4`$; its optimum is the value above | [Parameter family](science/parameter_family.md) |

## What is being compared

A binary access protocol assigns each surviving subset one of two actions: recover the unknown state with certainty, or always abort. A classical lottery chooses such a quantum protocol independently of the input. The comparison includes entangled encodings and general quantum secret-sharing codes.

Two disjoint subsets cannot both be deterministically authorized, because their holders could clone the unknown state. Among the five physical cycle edges, at most two can be pairwise intersecting. This gives the bound $`Q\le2`$ for every lottery. Uniformly routing the logical qubit to one of the five sites attains the bound.

The new code has fractional recovery probabilities whose sum exceeds two. Its encoding is deterministic; only its recovery is heralded. A zero assigned recovery probability is an abort decision and does not assert secrecy.

## How the code works

Each carrier contains a four-level system and one flag qubit. Two sparse, cyclically invariant source states are combined into an isometry. The pair filter cancels every wrong logical output and gives the same erased-environment state for both logical amplitudes. Copied coherent flags balance unequal source norms without changing those matching amplitudes.

The flag-conditioned branches have input-dependent weights. They therefore do not constitute an input-independent lottery over ordinary encoding channels. After the pair filter and its conditional correction, the complete successful operation is a constant times the identity channel.

The [physical interpretation](science/interpretation.md) proves a useful comparison: normalizing the same two source states separately into an unflagged code limits its optimal pair success to exactly $`2/5`$, even with an arbitrary decoder. It also accounts for the carrier dimensions and the correlated-erasure channel.

## Read the science

The complete account is organized by the role of each argument.

1. **[Model and theorem](science/model.md):** exact conclusive recovery, physical assumptions, the five-pair task, and the principal statements.
2. **[Construction](science/construction.md):** the source amplitudes, parameter domain, and normalized physical isometry.
3. **[Recovery](science/recovery.md):** physical Kraus operators, contraction bounds, cancellation identities, and all five exact logical channels.
4. **[Parameter family](science/parameter_family.md):** elementary optimization, the strict-advantage interval, and the rational example.
5. **[Access profiles](science/access_profiles.md):** the arbitrary-code benchmark, five-carrier minimality, and the secondary compatible-measurement interpretation.
6. **[Interpretation](science/interpretation.md):** why the flag helps, the unflagged comparison, resources, and correlated erasures.

[Related work](references/RELATED_WORK.md) attributes the imported results and compares the construction with probabilistic QEC, secret sharing, recovery-probability bounds, and contextuality. Machine-readable citations are in [references.bib](references/references.bib).

## Reproduce the finite checks

From the repository root, with Python 3.11 or later:

```sh
python -S verification/verify_exact.py --check verification/expected/exact_certificate.json
python -S verification/verify_family.py
```

The first command reconstructs all five channels of the rational member using exact rational number-field arithmetic. It checks the encoding isometry, physical decoder contraction, every effective logical Kraus operator, disjoint-pair joint-success products, and the binary-profile score. The second checks the parameter identities and family optimization algebra. Both use only Python's standard library.

An optional independent tensor reconstruction checks the optimal member, rational member, parameter boundaries, and conjugate optimum:

```sh
python -m pip install -r verification/requirements.txt
python verification/verify_family.py --numerical
```

These floating-point diagnostics corroborate the formulas. The exact theorem rests on the written proof; the rational example also has a finite certificate with no numerical tolerance. See [Verification](verification/README.md) for the commands, expected outputs, and proof boundaries.

## Scope

The result concerns a specified correlated-erasure distribution: one of five adjacent pairs survives. It gives exact conclusive recovery, with a failure flag on unsuccessful runs. The five carriers have local dimension eight, equivalent to fifteen physical qubits grouped into five erasable blocks.

The displayed family is optimized analytically. The unrestricted pentagon optimum remains between the attained score $`16/(1+4\sqrt3)`$ and the established upper bound $`\sqrt5`$. The construction does not settle saturation of that upper bound. Its significance is the strict separation above two and the resulting minimal carrier number.

The operational model and its limits are developed in [Model](science/model.md) and [Related work](references/RELATED_WORK.md).

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
