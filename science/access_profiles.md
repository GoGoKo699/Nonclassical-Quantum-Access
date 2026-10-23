# Recovery profiles beyond deterministic access structures

An exact recovery probability describes more than whether a set of carriers is authorized. A single encoding can admit several alternative, conclusive recovery operations, each of which either returns the unknown logical state perfectly or reports failure.

The construction in this repository encodes one qubit into five carriers and achieves

```math
\sum_{i=0}^{4}q_{\{i,i+1\}}
=\frac{16}{1+4\sqrt3}
\approx2.018111737966131>2.
```

Indices are modulo five. Every input-independent classical mixture of deterministic quantum access protocols satisfies the bound $`2`$, even when its encodings and carrier dimensions are unrestricted. Five is the smallest carrier number for this separation in the finite, unrestricted-dimension model.

## Operational probabilities and optimal capabilities

Let $`L\cong\mathbb C^K`$, with $`K>1`$, be the logical system. An encoder $`\mathcal E`$ maps it into carriers $`B_0,\ldots,B_{n-1}`$. For a surviving subset $`S`$, an exact successful decoder is a completely positive trace-nonincreasing map satisfying

```math
\begin{gathered}
\mathcal R_S\circ\operatorname{Tr}_{S^c}\circ\mathcal E
=q_S\operatorname{id}_L.
\end{gathered}
\tag{1}
```

This is equality of linear maps. It includes logical off-diagonal operators and inputs entangled with an inaccessible reference. Success has probability $`q_S`$ for every logical input. A completed instrument reports failure otherwise.

The encoder is fixed before the surviving subset is known. The decoder knows the erasure locations and may act jointly on the retained carriers. Different subset decoders are alternative operations. See [the model](model.md) and [the recovery proof](recovery.md).

For a fixed finite-dimensional encoder, its optimal probability

```math
p^*_{\mathcal E}(S)=
\max_{\mathcal R_S}
\left\{p:\mathcal R_S\circ\operatorname{Tr}_{S^c}\circ\mathcal E
=p\operatorname{id}_L\right\}
```

is monotone under inclusion: a larger subset can discard its extra carriers. The maximum is attained because the feasible decoder Choi operators form a compact set.

An *operational* vector $`q=(q_S)`$ need not be monotone. A decoder may deliberately abort on a larger subset or reject some otherwise successful outputs. Thus $`q_S=0`$ does not imply that recovery is impossible, and even $`p^*_{\mathcal E}(S)=0`$ does not imply secrecy. This operational convention agrees with the probability body studied by [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026).

## The deterministic-mixture benchmark

Fix a family $`\mathcal F`$ of nonempty queried subsets. A **binary protocol profile** is an achievable vector

```math
b\in\{0,1\}^{\mathcal F}.
```

At a query with $`b_S=1`$, recovery is deterministic and exact. At a query with $`b_S=0`$, the protocol always aborts. The zero may be deliberate even if the encoder would permit recovery.

For comparison, the deterministic-capability indicator of a fixed encoder,

```math
a_{\mathcal E}(S)=\mathbf 1\{p^*_{\mathcal E}(S)=1\},
```

is monotone. Every binary protocol implemented with that encoder is a coordinatewise subprofile of $`a_{\mathcal E}`$. We do not assume that the encoder's full optimal heralded profile contains only zero and one entries. In particular, an isometric encoder is a deterministic physical operation but can have fractional exact recovery probabilities.

Let $`\mathcal B_{n,K}(\mathcal F)`$ denote the binary protocol profiles and define

```math
\begin{gathered}
\mathcal C_{n,K}(\mathcal F)
=\operatorname{conv}\mathcal B_{n,K}(\mathcal F).
\end{gathered}
\tag{2}
```

This benchmark permits an input-independent lottery over arbitrary quantum encodings with binary access decisions. A code label can be copied into the erasable carriers so that every nonempty survivor can select the corresponding decoder. The benchmark includes arbitrary deterministic quantum secret-sharing schemes and entangled encodings; its upper bounds do not assume routing, stabilizer codes, or classical storage.

Additional independent aborts do not enlarge (2). Given $`0\le q\le p\in\mathcal C`$, presample an acceptance coin for each query with probability $`q_S/p_S`$ when $`p_S>0`$. Combining these coins with the original lottery produces a lottery over binary subprofiles with mean $`q`$. Consequently, $`\mathcal C`$ is downward closed. Equivalently, it is the downward convex hull of deterministic monotone capability profiles.

## Why disjoint exact recoveries are exclusive

Suppose $`S\cap T=\varnothing`$. Apply completed recovery instruments to these disjoint systems simultaneously, and let $`\mathcal J`$ be the completely positive map for both instruments succeeding. Its first logical marginal is a CP submap of $`q_S\operatorname{id}_L`$, and its second is a CP submap of $`q_T\operatorname{id}_L`$.

The identity channel has a rank-one Choi operator. Every CP submap of a multiple of the identity is therefore itself a multiple of the identity. The two marginals of $`\mathcal J`$ must be $`c\operatorname{id}_L`$ with the same $`c\ge0`$, because their traces agree. If $`c>0`$, the channel $`\mathcal J/c`$ reproduces every input in both outputs. For pure inputs, both marginals are pure, so the joint output consists of two copies of the input. No-cloning excludes this for $`K>1`$. Hence $`\mathcal J=0`$.

Applying this reasoning to any pairwise disjoint family gives

```math
\begin{gathered}
\sum_{S\in\mathcal K}q_S\le1
\qquad
\text{for every family }\mathcal K\text{ of pairwise disjoint queries.}
\end{gathered}
\tag{3}
```

This exclusivity statement applies to exact probabilistic recovery, not only deterministic recovery.

## Binary profiles and the disjointness graph

Define $`G_{\mathcal F}`$ to have one vertex for each queried subset and an edge between disjoint subsets.

A binary profile's successful subsets must be pairwise intersecting by (3), so they form an independent set of $`G_{\mathcal F}`$. The converse is also available with unrestricted finite dimensions. For an independent query family, take its upward closure and extend it to a maximal intersecting monotone family on the same carriers. [Gottesman's general-access theorem](../references/RELATED_WORK.md#gottesman2000) supplies a pure-state QSS realization of that maximal family. Recover on the requested members and deliberately abort on the others. A sufficiently large logical alphabet can be restricted to the desired logical dimension.

Thus

```math
\begin{gathered}
\mathcal C_{n,K}(\mathcal F)
=\operatorname{STAB}(G_{\mathcal F}),
\end{gathered}
\tag{4}
```

where $`\operatorname{STAB}(G)`$ is the convex hull of indicators of independent sets. This identification follows from established no-cloning and QSS realization results.

The use of QSS proves that all independent sets are attainable. It does not impose secrecy on every competing protocol: a code leaking information at an aborting query is still covered by the same bound.

## The pentagon bound is exactly two

For the five queries

```math
S_i=\{i,i+1\},\qquad i=0,\ldots,4,
```

the disjointness graph is a five-cycle in the order $`S_0,S_2,S_4,S_1,S_3`$. This is a graph of *queries*; its adjacency means physical disjointness.

At most two physical cycle edges can be pairwise intersecting. Once $`\{0,1\}`$ is included, the only other cycle edges meeting it are $`\{1,2\}`$ and $`\{4,0\}`$, which are disjoint from one another. Therefore

```math
\begin{gathered}
\boxed{\sum_{i=0}^{4}q_{S_i}\le2
\quad\text{for every }q\in\mathcal C_{5,K}(\mathcal F).}
\end{gathered}
\tag{5}
```

The bound is sharp. Placing the whole logical system at one carrier allows deterministic recovery from its two incident edges. A uniform lottery over the five carrier choices yields $`q_{S_i}=2/5`$ for every query. Routing establishes attainability; the upper bound covers all deterministic quantum access protocols.

The [explicit construction](construction.md) and [recovery identities](recovery.md) attain

```math
\begin{gathered}
q_{S_i}=\frac{16}{5(1+4\sqrt3)}.
\end{gathered}
\tag{6}
```

Its strict violation of (5) follows from $`7>4\sqrt3`$, or equivalently $`49>48`$. No optimality assumption about the chosen decoders is needed. The encoder's optimized probabilities are at least these values and therefore also violate (5).

For uniformly random adjacent-pair survival, this means exact recovery with probability approximately $`0.403622347593226`$, compared with the deterministic-mixture optimum $`0.4`$. The gain is approximately $`0.362235`$ percentage points. The result is a strict separation of feasible recovery profiles.

## Five-carrier minimality

[Alhejji et al.](../references/RELATED_WORK.md#alhejji2026) characterize the full operational recovery-probability body for four or fewer carriers. Their constructive proof realizes its extreme profiles using binary access patterns, permutations, coordinatewise reductions, mixing, and unused carriers. Each operation preserves the deterministic-mixture body. It follows that

```math
\begin{gathered}
\mathcal Q_{n,K}=\mathcal C_{n,K}
\qquad(n\le4,\ K>1),
\end{gathered}
\tag{7}
```

when carrier dimensions are finite but unrestricted.

The inference uses that constructive proof, not just equality with a partition-constraint polytope. The new three-carrier binary pattern authorizes all subsets of size at least two; the new four-carrier pattern authorizes all triples and the pairs containing a distinguished carrier. Logical-qubit realizations can be obtained from a three-qutrit threshold code and a five-qubit distance-three code with two qubits bundled into one carrier, respectively. The required threshold constructions are established [QSS constructions](../references/RELATED_WORK.md#cleve1999). The remaining operations preserve mixtures of binary profiles, including deliberate aborts.

Restricting a full profile to any query family preserves its convex-mixture representation. Consequently, no query family on four or fewer carriers can produce this separation, while (6) does so on five.

This minimality counts carrier blocks. It does not establish minimal physical-qubit count, local dimension, or circuit cost. A benchmark restricted to specified small local dimensions would be a different comparison.

## Perfect query graphs: standard structural context

Let $`\operatorname{QSTAB}(G)`$ be the polytope defined by nonnegativity and all clique inequalities. Equations (3) and (4) imply

```math
\begin{gathered}
\operatorname{STAB}(G_{\mathcal F})
\subseteq\mathcal Q_{n,K}(\mathcal F)
\subseteq\operatorname{QSTAB}(G_{\mathcal F}).
\end{gathered}
\tag{8}
```

The [standard perfect-graph polyhedral characterization](../references/RELATED_WORK.md#chvatal1975) gives $`\operatorname{STAB}(G)=\operatorname{QSTAB}(G)`$ for perfect graphs. Every operational profile on such a query family is consequently a deterministic-profile mixture. This is an immediate consequence of established results, not a new graph-theoretic claim.

The pentagon is the smallest imperfect graph. Its independent-set inequality allows a separation that clique constraints alone cannot exclude. This motivates the query family, but graph size alone does not prove carrier minimality: graph vertices are subsets rather than carriers. Equation (7) supplies that separate conclusion.

## Secondary interpretation as compatible-measurement contextuality

The [pentagon contextuality inequality and graph approach](../references/RELATED_WORK.md#cabello2014) are established results. The comparison in (5) requires no hidden-variable assumption; it concerns explicitly defined quantum protocols.

For this construction there is also a concrete compatible-measurement interpretation. The success effect

```math
P_i=\sum_{\ell}K_{i,\ell}^{\dagger}K_{i,\ell}
```

is a projector because the stacked decoder rows are orthonormal. Output corrections leave it unchanged. Disjoint queried pairs give commuting projectors. The joint-success argument above implies

```math
\operatorname{Tr}\!\left[P_iP_j\mathcal E(\rho)\right]=0
\qquad(S_i\cap S_j=\varnothing)
```

for every encoded logical input.

To define the corresponding measurement experiment, prepare an encoded state and measure each disjoint pair of success tests as a separate compatible context. For the [rational parameter member](parameter_family.md) with $`x=1/8`$, exact arithmetic verifies every such context distribution:

| Outcomes of the two success tests | Probability |
|---|---:|
| $`00`$ | $`107/555`$ |
| $`10`$ | $`224/555`$ |
| $`01`$ | $`224/555`$ |
| $`11`$ | $`0`$ |

These probabilities are independent of the logical input. Any global distribution over five predetermined binary outcomes reproducing these context distributions must be supported on independent sets of the cycle, and would satisfy $`\sum_iq_i\le2`$. Here the sum is $`224/111>2`$. Equivalently, for $`A_i=I-2P_i`$,

```math
\sum_{\{i,j\}\in E(C_5)}\langle A_iA_j\rangle
=5-4\frac{224}{111}
=-\frac{341}{111}<-3.
```

This is an ideal compatible-context marginal violation under a common-observable, noncontextual global-assignment assumption. It is secondary to the recovery-profile theorem. It does not establish a new contextuality inequality, Bell nonlocality, or device-independent certification. The violation holds throughout the encoded subspace, not for every state of the physical Hilbert space. Both successful and failed test outcomes enter these statistics; no successful-run postselection is used.
