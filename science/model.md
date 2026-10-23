# Exact recovery after a pair survives

An unknown qubit is encoded into five physical carriers. Three carriers are erased, leaving one adjacent pair of a cycle. The receiver knows which pair survived and may act jointly on those two carriers. Recovery may fail, but every accepted output must reproduce the input exactly.

The question is whether the resulting success probabilities can always be explained by a classical lottery over deterministic quantum access patterns. Such a pattern specifies which surviving sets recover with certainty and which queries always abort. The construction in this project gives a negative answer at the smallest possible carrier number.

## Encoding and heralded recovery

Let $`L\simeq\mathbb C^K`$ be the logical system, with $`K>1`$, and let $`B_0,\ldots,B_{n-1}`$ be distinguishable carriers of arbitrary finite dimensions. An encoder is a completely positive trace-preserving map

```math
\mathcal E:\mathcal B(L)\longrightarrow
\mathcal B\!\left(\bigotimes_{j=0}^{n-1}B_j\right).
```

For a surviving set $`S`$, the accessible channel is

```math
\mathcal N_S=\operatorname{Tr}_{S^c}\circ\mathcal E.
```

A successful recovery operation $`\mathcal R_S`$ is completely positive and trace-nonincreasing. Exact heralded recovery with probability $`q_S`$ means

```math
\boxed{\mathcal R_S\circ\mathcal N_S=q_S\,\operatorname{id}_L.}
\tag{1}
```

This is an equality of linear maps. It fixes the action on logical coherences as well as on basis states. Consequently, the success probability is independent of the logical input, and recovery preserves entanglement with an arbitrary inaccessible reference. The failure operation can output a classical failure flag; its quantum state has no recovery guarantee.

The encoder is selected before the erasure pattern is known. A decoder can use fresh local ancillas and joint operations on its surviving set. Erased carriers, a retained sender system, preshared sender-receiver entanglement, and a noiseless quantum side channel are not available. All flags in the construction are stored in the carriers and undergo the same erasures.

The complete achievable probability body is denoted by $`\mathcal Q_{n,K}`$. It is the operational body of [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026), with finite but otherwise unrestricted carrier dimensions.

## Probabilities describe a protocol

A recovery protocol may deliberately abort even when another decoder could succeed. Therefore $`q_S=0`$ is an assigned abort probability, not a secrecy statement about the reduced state on $`S`$. The optimized probability for a fixed encoder,

```math
p_{\mathcal E}^{\max}(S)=
\max_{\mathcal R_S}
\left\{p:\mathcal R_S\circ\mathcal N_S=p\,\operatorname{id}_L\right\},
```

is monotone under inclusion of surviving sets. An assigned operational tuple $`q`$ need not be monotone, because its decoders may discard successful outcomes separately for different queries.

A **binary protocol profile** assigns each queried set probability zero or one in (1). Let $`\mathcal C_{n,K}`$ be the convex hull of these profiles. Operationally, it permits an input-independent classical lottery over arbitrary quantum encodings with binary recovery decisions. The sampled code label may be copied into each erasable carrier. Additional independent aborts are already included.

This benchmark includes arbitrary deterministic quantum secret-sharing schemes and arbitrary entangled encoders. It does not mean that the encoding channel itself is probabilistic: the new encoder below is a deterministic isometry. The distinction concerns whether its *recovery probabilities* belong to the binary-profile convex hull. [Access profiles](access_profiles.md) develops this definition and its graph representation.

## The five-pair erasure task

Use site labels modulo five and define

```math
S_i=\{i,i+1\},\qquad i=0,1,2,3,4.
```

Local decoder matrices use the ordered pairs $`(0,1),(1,2),(2,3),(3,4),(4,0)`$. In particular, the wraparound order is $`(4,0)`$.

The physical channel chooses an adjacent pair uniformly, transmits that pair, and reports its label:

```math
\mathcal N_{C_5}(\sigma)
=\frac15\sum_{i=0}^4
|i\rangle\langle i|_C\otimes
\operatorname{Tr}_{S_i^c}\sigma.
\tag{2}
```

Every carrier survives with probability $`2/5`$, but the erasures are correlated. The receiver is guaranteed one of these five pairs, rather than a uniformly chosen pair among all ten two-element subsets.

For a profile $`q_i=q_{S_i}`$, write

```math
Q=\sum_{i=0}^4q_i,\qquad
\overline q=\frac Q5.
```

The score $`Q`$ compares the five alternative recovery operations; it does not mean that all five pairs are queried together in a transmission.

## Main theorem

**Theorem 1: exact access beyond deterministic-profile mixtures.**
There is an isometry

```math
V:\mathbb C^2\longrightarrow(\mathbb C^8)^{\otimes5}
```

and a successful recovery operation on each adjacent pair such that

```math
\mathcal R_i\circ\operatorname{Tr}_{S_i^c}\circ\mathcal V
=p_{\mathrm{code}}\,\operatorname{id}_2,
\qquad
\mathcal V(\rho)=V\rho V^\dagger,
```

where

```math
\boxed{
p_{\mathrm{code}}=\frac{16}{5(1+4\sqrt3)}
=0.403622347593226\ldots .
}
\tag{3}
```

The same pair decoder is used after relabeling each ordered pair. In contrast, every classical mixture of binary exact-access profiles, with arbitrary finite carrier dimensions, obeys

```math
Q\le2,\qquad \overline q\le\frac25.
\tag{4}
```

The construction has

```math
Q=\frac{16}{1+4\sqrt3}>2,
```

so its five displayed probabilities lie outside that convex hull. Every extension to a complete operational profile is outside the full binary-profile convex hull as well.

**Minimality corollary.** Five is the minimum number of carriers for this separation when carrier dimensions are finite and unrestricted. The new five-carrier construction supplies sufficiency. Necessity follows from the constructive characterization of $`\mathcal Q_{n,K}`$ for $`n\le4`$ in [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026), together with the closure argument in [Access profiles](access_profiles.md).

Minimality concerns the number of carrier blocks. It does not assert minimal physical-qubit count or minimal local dimension.

## A simpler exact member

The construction belongs to an explicit one-parameter family. At $`x=1/8`$, the pair success and total score are rational:

```math
\boxed{
q_i=\frac{224}{555}
=\frac25+\frac2{555},\qquad
Q=\frac{224}{111}=2+\frac2{111}.
}
\tag{5}
```

The [exact verifier](../verification/verify_exact.py) contracts every effective logical Kraus operator of this member using rational arithmetic in a specified number field. The stronger value (3) follows from the elementary family optimization in [Parameter family](parameter_family.md).

## Proof and reading route

| Step | Scientific content | Authoritative page |
|---|---|---|
| Define the code | Two sparse cyclic source states and a flagged isometry | [Construction](construction.md) |
| Verify the channel | Physical Kraus operators, cancellation of false outcomes, exact logical map | [Recovery](recovery.md) |
| Evaluate the attainable score | The full parameter interval, rational member, and exact family optimum | [Parameter family](parameter_family.md) |
| Establish the separation | Arbitrary-dimension binary-profile bound and five-carrier minimality | [Access profiles](access_profiles.md) |
| Understand the mechanism | Coherent flags, a comparison with separately normalized source states, and resource accounting | [Interpretation](interpretation.md) |
| Reproduce finite identities | Exact number-field certificate and full numerical tensor contractions | [Verification](../verification/README.md) |

The result determines an attained lower bound, not the unrestricted optimum. The known universal pentagon inequality of [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026) gives

```math
\frac{16}{5(1+4\sqrt3)}
\le
\sup_{\mathcal E,\{\mathcal R_i\}}\overline q
\le
\frac1{\sqrt5}.
\tag{6}
```

The supremum in (6) permits arbitrary finite carrier dimensions. Neither equality at its right endpoint nor optimality of the displayed code is established here.
