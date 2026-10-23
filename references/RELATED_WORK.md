# Related work and scope of the contribution

The contribution is an explicit exact-recovery profile outside the convex hull of deterministic quantum access protocols. It combines a new finite-dimensional construction with established recovery-probability bounds, QSS existence theorems, and the small-carrier classification.

The achieved pentagon sum is

```math
\frac{16}{1+4\sqrt3}\approx2.018111737966131,
```

above the deterministic-mixture optimum $`2`$. The universal upper bound remains $`\sqrt5`$. The attained value is not claimed to be globally optimal.

## Direct recovery-profile precedent

<a id="alhejji2026"></a>
### Alhejji et al.: exact recovery after erasure

**M. A. Alhejji, N. Lordi, O. Baraskar, A. Shlosberg, and E. Knill, “Constraints on recovering quantum information after erasure,” arXiv:2607.17319v2 (2026).**

[Manuscript](https://arxiv.org/html/2607.17319v2) · [arXiv record](https://arxiv.org/abs/2607.17319)

This is the closest direct precedent. It defines the operational recovery-probability body, permits finite but unrestricted carrier dimensions, proves its convexity and downward closure, and gives a constructive characterization for up to four carriers. It also bounds sums of exact recovery probabilities by the Lovász number of the query family's disjointness graph.

Its Eq. (13) gives the five-cycle bound $`\sum_iq_{\{i,i+1\}}\le\sqrt5`$ and asks whether that bound is attainable. The manuscript supplies no pentagon construction above the deterministic-profile value $`2`$.

The present construction gives a strict lower bound beyond that deterministic hull. Its five-carrier minimality uses the attributed small-carrier characterization. It leaves the Lovász-saturation question open. The elementary benchmark $`2`$ is not claimed as a new graph inequality.

## Deterministic quantum secret-sharing structures

<a id="gottesman2000"></a>
### Gottesman: general access structures

**D. Gottesman, “Theory of quantum secret sharing,” Physical Review A 61, 042311 (2000), arXiv:quant-ph/9910067.**

[Manuscript](https://arxiv.org/html/quant-ph/9910067v1) · [DOI](https://doi.org/10.1103/PhysRevA.61.042311)

Theorem 8 establishes realizability of monotone quantum access structures satisfying no-cloning, with pure-state realizations for maximal structures. This supplies the deterministic profiles in the benchmark: an intersecting query family can be extended to a maximal monotone one, realized by a QSS code, and restricted operationally by deliberate aborts.

The upper bound covers more than secret-sharing schemes. We impose exact retrieval on successful queries, without requiring secrecy on every other subset. A zero operational probability may be a deliberate abort; even zero *optimal* exact recovery probability does not imply no information leakage. For example, a proper subset of a repetition encoding retains logical basis populations while losing logical coherence.

<a id="cleve1999"></a>
### Cleve, Gottesman, and Lo: threshold constructions

**R. Cleve, D. Gottesman, and H.-K. Lo, “How to Share a Quantum Secret,” Physical Review Letters 83, 648–651 (1999), arXiv:quant-ph/9901025.**

[Manuscript](https://arxiv.org/abs/quant-ph/9901025) · [DOI](https://doi.org/10.1103/PhysRevLett.83.648)

Threshold QSS constructions provide concrete realizations underlying the small-carrier classification. The comparison includes such quantum encodings, arbitrary entangled encodings, and classical mixtures of their binary access decisions. It is not a comparison against storing classical data.

## Probabilistic correction

<a id="kukulski2023"></a>
### Kukulski, Pawela, and Puchała: probabilistic QEC

**R. Kukulski, Ł. Pawela, and Z. Puchała, “On the probabilistic quantum error correction,” IEEE Transactions on Information Theory 69, 4620–4640 (2023), arXiv:2206.05232.**

[Manuscript](https://arxiv.org/html/2206.05232v1) · [DOI](https://doi.org/10.1109/TIT.2023.3254054)

This work develops general conclusive correction conditions and exhibits noise channels correctable probabilistically but not deterministically. It also shows that mixed encodings can improve success under fixed resource and noise constraints.

Accordingly, the broad claim that probabilistic QEC can outperform deterministic correction is established prior work. The present result concerns a simultaneous vector of exact erasure-subset recovery probabilities for one encoding. That vector cannot be reproduced by an input-independent lottery over binary quantum access profiles.

The new encoder is itself an isometry. Its copied flag does not select ordinary encoders through input-independent classical randomness: the normalized flag-conditioned branches are filtered maps, and their occurrence weights depend on logical populations. The complete encoder remains deterministic, while its successful recovery probability is input-independent.

## Independent and correlated erasures

<a id="ahmed2026"></a>
### Ahmed and Smith: distributed monogamy and channel simulation

**R. G. Ahmed and G. Smith, “Distributed Monogamy of Entanglement limits Quantum Channel Simulation,” arXiv:2607.08591v2 (2026).**

[Manuscript](https://arxiv.org/html/2607.08591v2) · [arXiv record](https://arxiv.org/abs/2607.08591)

Distributed monogamy bounds average exact EPR extraction from a uniformly random $`k`$-subset by $`k/n`$ when $`k\le n/2`$. This work and Alhejji et al. prove independent-erasure nonamplification in the anti-degradable regime.

The channel studied here instead uniformly retains one of five *adjacent* pairs. It has correlated erasures, although each carrier individually survives with probability $`2/5`$. The construction does not exceed the all-pairs bound: its five diagonal-pair probabilities must have average at most

```math
\frac45-\frac{16}{5(1+4\sqrt3)}
\approx0.396377652406774.
```

Thus an improvement on the chosen adjacent-pair family is compatible with the bound for all ten pairs and with independent-erasure nonamplification. The strict comparison is against all deterministic access mixtures for the same specified query distribution.

<a id="cubitt2008"></a>
### Cubitt, Ruskai, and Smith: anti-degradable channels

**T. S. Cubitt, M. B. Ruskai, and G. Smith, “The structure of degradable quantum channels,” Journal of Mathematical Physics 49, 102104 (2008), arXiv:0802.1360.**

[Manuscript](https://arxiv.org/html/0802.1360v2) · [DOI](https://doi.org/10.1063/1.2953685)

Anti-degradable channels have zero unassisted quantum capacity. The particular correlated-erasure channel here is anti-degradable: its environment holds the complementary triple and pair label, and can choose one of the two cycle edges in that triple to reproduce the receiver's channel. The conclusive logical transmission probability remains below one half. No positive-capacity or independent-erasure-amplification claim follows from the construction.

## Graphs and contextuality

<a id="chvatal1975"></a>
### Chvátal: the perfect-graph polyhedral characterization

**V. Chvátal, “On certain polytopes associated with graphs,” Journal of Combinatorial Theory, Series B 18, 138–154 (1975).**

[DOI](https://doi.org/10.1016/0095-8956(75)90041-6) · [Author's publication list](https://users.encs.concordia.ca/~chvatal/publ.html)

For a perfect graph, clique inequalities and nonnegativity describe its stable-set polytope. Combining this standard result with disjoint-recovery no-cloning and Gottesman's access-structure realizations shows that every operational profile on a perfect query graph is a deterministic-profile mixture.

The pentagon is the smallest imperfect graph. This explains the obstruction at the level of queried subsets; it does not alone prove minimal carrier number, since graph vertices represent queries. The carrier-minimality claim uses Alhejji et al.'s separate classification. The polyhedral observation is attributed background, not a new theorem.

<a id="cabello2014"></a>
### Cabello, Severini, and Winter: the graph approach to contextuality

**A. Cabello, S. Severini, and A. Winter, “Graph-Theoretic Approach to Quantum Correlations,” Physical Review Letters 112, 040401 (2014), arXiv:1401.7081.**

[Manuscript](https://arxiv.org/html/1401.7081v1) · [DOI](https://doi.org/10.1103/PhysRevLett.112.040401)

The independence number, stable-set polytope, and Lovász number already appear in contextuality. Their appearance in a recovery problem does not make those graph quantities new.

An arbitrary orthogonal representation need not provide tensor-local decoders for a common encoding of an unknown quantum input. The contribution here is an explicit realization satisfying those exact recovery requirements.

The success projectors also admit a secondary ideal compatible-measurement interpretation. Disjoint pairs give commuting tests with zero joint-success probability, while the sum of single-test probabilities exceeds two. This excludes a global distribution of predetermined outcomes reproducing all compatible contexts. The [precise statement](../science/access_profiles.md#secondary-interpretation-as-compatible-measurement-contextuality) includes the compatibility and common-observable assumptions. It is not a new contextuality inequality or a device-independent certification.

<a id="klyachko2008"></a>
### Klyachko et al.: the pentagon noncontextuality inequality

**A. A. Klyachko, M. A. Can, S. Binicioğlu, and A. S. Shumovsky, “Simple Test for Hidden Variables in Spin-1 Systems,” Physical Review Letters 101, 020403 (2008), arXiv:0706.0126.**

[Manuscript](https://arxiv.org/abs/0706.0126) · [DOI](https://doi.org/10.1103/PhysRevLett.101.020403)

The five-cycle inequality and quantum violation are established. Our rational construction gives a particular tensor-local compatible-context realization with probabilities $`224/555`$, not a new inequality. The violation is uniform over the encoded logical subspace; no claim of state independence on the entire physical Hilbert space is made.

## Neighboring entanglement-sharing work

<a id="khanian2025"></a>
### Khanian et al.: entanglement sharing

**Z. Khanian, D. Lee, D. Leung, Z. Li, A. May, S. Miao, T. Mori, F. Salek, J. Yi, and B. Yoshida, “Entanglement sharing schemes,” arXiv:2509.21462 (2025), version 3 (2026).**

[Manuscript](https://arxiv.org/html/2509.21462v3) · [arXiv record](https://arxiv.org/abs/2509.21462)

This work studies deterministic EPR extraction between two variable groups, with known or unknown partner and constraints on unauthorized pairings. Its pentagon summoning obstruction concerns a communication-constrained unknown-partner task. Here the reference is fixed and inaccessible, a single requested subset applies a joint conclusive decoder, and the object is a vector of recovery probabilities. Definitions 17 and 24 in version 3 impose deterministic channel output, rather than the conclusive profile separation constructed here.

## Educational anchor

<a id="watrous2018"></a>
### Watrous: mathematical foundations

**J. Watrous, The Theory of Quantum Information, Cambridge University Press (2018).**

[Author's book page and chapter manuscripts](https://cs.uwaterloo.ca/~watrous/TQI/)

This is the repository's single educational anchor. Its finite-dimensional treatment of states, channels, measurements, and entanglement supplies the language for exact conclusive recovery. The [source-to-project bridge](../learning/WATROUS_BRIDGE.md) identifies the relevant sections, translates notation, and derives the additional steps needed here. The [thirty-milestone map](../learning/MILESTONES.md) organizes the project's scientific argument.

The book is a foundation for understanding the construction. The exact access-profile separation is proved in this repository; the general QSS realizability theorem and the small-carrier classification remain separately attributed research dependencies above. The author's manuscript is linked at its source and is not redistributed here.

## Scope of the result

| Established here | Not established |
|---|---|
| An exact profile outside all deterministic quantum-access mixtures | Global optimality or saturation of the Lovász bound |
| An isometric logical-qubit construction with five finite-dimensional carriers | Minimum local dimension or physical-qubit count |
| Five-carrier minimality in the unrestricted finite-dimension model | A classification under fixed small carrier dimensions |
| Exact conclusive recovery from five specified pairs | Perfect secrecy for every failed or unqueried subset |
| Improvement for the specified correlated erasure distribution | Independent-erasure amplification or positive unassisted capacity |
| An explicit compatible-context corollary under stated assumptions | Bell nonlocality or device-independent certification |

