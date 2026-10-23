# From Watrous to nonclassical quantum access

**Educational anchor:** John Watrous, *The Theory of Quantum Information* (2018), through the [author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/). This bridge uses the finite-dimensional channel formalism in that book to explain the project's exact recovery statement. Chapter links below point to the author's copies; the repository does not reproduce the book.

The central object is an equality of quantum operations:

```math
\mathcal R_S\circ\mathrm{Tr}_{S^c}\circ\mathcal E
=q_S\mathrm{id}_L.
```

An encoder distributes an unknown logical system among physical carriers. A specified subset survives. Its decoder either reports failure or returns the original quantum information exactly, with probability $`q_S`$. The purpose of this bridge is to derive what that equality requires and then connect it to the five-carrier construction.

The book supplies the mathematical language of states, channels, and instruments; it is not a general treatment of quantum error correction or fault tolerance. The source states, recovery amplitudes, strict pentagon separation, and optimized parameter family are project results. The small-carrier classification and universal pentagon upper bound are separate research inputs, attributed below and in [Related work](../references/RELATED_WORK.md). They are not theorems from the educational anchor. The [anchor reference](../references/RELATED_WORK.md#watrous2018) records the book's role.

<a id="verified-reading-map"></a>
## Verified reading map

The section numbers and titles below follow the author's [official table of contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf). Page numbers are printed book pages, not page numbers within a chapter PDF.

| Watrous section | Printed page | Use here |
|---|---:|---|
| [1.1.1, Complex Euclidean spaces](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=1) | 1 | Vectors, orthogonality, tensor factors |
| [1.1.2, Linear operators](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=8) | 8 | Adjoints, positive operators, partial trace, vectorization |
| [1.2.1, Analysis and convexity](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=35) | 35 | Convex mixtures of protocol profiles |
| [2.1.1, Registers and classical state sets](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=1) | 58 | Carrier blocks and their internal registers |
| [2.1.2, Quantum states of registers](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4) | 61 | Density operators and mixtures |
| [2.1.3, Reductions and purifications of quantum states](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10) | 67 | Erasure, inaccessible references, pure encoders |
| [2.2.1, Definitions and basic notions concerning channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15) | 72 | Completely positive, trace-preserving maps |
| [2.2.2, Representations and characterizations of channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20) | 77 | Choi, Kraus, and Stinespring representations |
| [2.3.2, Basic notions concerning measurements](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=48) | 105 | Instruments, including retained quantum outputs |

Three precise results in Section 2.2.2 are useful: **Theorem 2.22**, p. 82, characterizes complete positivity; **Theorem 2.26**, p. 87, characterizes trace preservation; **Corollary 2.27**, p. 89, combines these into channel characterizations. The discussion of instruments is on pp. 111–113 within Section 2.3.2. The operator-vector correspondence is on pp. 23–24 within Section 1.1.2.

The derivations that follow fill the gap between those general tools and the project's particular operational claims.

<a id="notation-and-normalization"></a>
## Notation and normalization

All systems here are finite dimensional. Watrous writes vectors without Dirac notation and uses an asterisk for the adjoint. The project uses kets and a dagger. The translation is:

| Book notation | Project notation or meaning |
|---|---|
| $`u`$, $`uv^*`$ | $`\lvert u\rangle`$, $`\lvert u\rangle\langle v\rvert`$ |
| $`A^*`$ | $`A^\dagger`$ |
| $`E_{a,b}`$ | $`\lvert a\rangle\langle b\rvert`$ |
| $`\mathrm L(\mathcal X,\mathcal Y)`$ | Linear operators from $`\mathcal X`$ to $`\mathcal Y`$ |
| $`\mathrm L(\mathcal X)`$ | The operator space also written $`\mathcal B(\mathcal X)`$ in [the model](../science/model.md) |
| $`\mathbb 1_{\mathcal X}`$ | The identity operator $`I_{\mathcal X}`$ |
| $`\mathbb 1_{\mathrm L(\mathcal X)}`$ | The identity **map** $`\mathrm{id}_{\mathcal X}`$ |
| $`\mathrm C(\mathcal X,\mathcal Y)`$ | Completely positive, trace-preserving maps |

The logical system is $`L\simeq\mathbb C^K`$. It is a Hilbert space, not the operator-space symbol $`\mathrm L(\mathcal X)`$. The explicit construction has $`K=2`$. Physical carriers are $`B_0,\ldots,B_4`$, and $`A`$ denotes an inaccessible reference.

### Choi order and normalization

Watrous's Choi operator places the channel output first and uses an unnormalized maximally entangled vector. In the project's ket notation,

```math
J(\Phi)=
\sum_{a,b=0}^{K-1}\Phi(|a\rangle\langle b|)
\otimes |a\rangle\langle b|
\quad\text{on }Y\otimes L.
```

The project often places the reference first and uses

```math
|\Phi_K\rangle_{AL}
=\frac1{\sqrt K}\sum_{a=0}^{K-1}|a\rangle_A|a\rangle_L.
```

For a map $`\Phi:\mathcal B(L)\to\mathcal B(Y)`$, the corresponding operator is

```math
\omega_{AY}
=(\mathrm{id}_A\otimes\Phi)
\bigl(|\Phi_K\rangle\langle\Phi_K|\bigr)
=\frac1K\,\mathsf S J(\Phi)\mathsf S^\dagger,
```

where $`\mathsf S`$ exchanges the two factors and identifies the input copy with $`A`$. Thus the two conventions differ by a factor $`K`$ and a permutation, not by a physical operation on the input.

For a trace-preserving encoder, $`\mathrm{Tr}_Y\omega_{AY}=I_A/K`$. For a successful map $`q\mathrm{id}_L`$, one has

```math
\omega_{AL}=q|\Phi_K\rangle\langle\Phi_K|,
\qquad \mathrm{Tr}\omega_{AL}=q.
```

This normalization matters: a normalized source vector with a biased reference marginal does not automatically describe a trace-preserving encoder. [Construction](../science/construction.md#reference-state-formulation) addresses exactly this issue.

<a id="exact-conclusive-recovery"></a>
## Exact conclusive recovery

### Complete positivity and success probability are separate requirements

A Kraus expression

```math
\mathcal R(\sigma)=\sum_a R_a\sigma R_a^\dagger
```

guarantees complete positivity, as in Watrous's Theorem 2.22. It does not by itself make $`\mathcal R`$ an allowed successful operation. For example, $`\sigma\mapsto2\sigma`$ is completely positive but assigns probability two to every normalized input.

To derive the additional condition, put

```math
E_{\mathrm{succ}}=\sum_aR_a^\dagger R_a.
```

Then

```math
\mathrm{Tr}\mathcal R(\sigma)
=\mathrm{Tr}(E_{\mathrm{succ}}\sigma).
```

This is no larger than $`\mathrm{Tr}\sigma`$ for every positive $`\sigma`$ exactly when $`E_{\mathrm{succ}}\le I`$. Necessity follows by testing an eigenvector with eigenvalue greater than one if such an eigenvector exists. Therefore:

```math
\begin{aligned}
\text{successful quantum operation:}&\quad
\mathcal R\text{ is CP},\quad E_{\mathrm{succ}}\le I,\\
\text{channel:}&\quad
\mathcal R\text{ is CP},\quad E_{\mathrm{succ}}=I.
\end{aligned}
```

The inequality is the condition for **trace nonincrease**. It permits a failure outcome. One explicit completion outputs the successful state in $`L`$ and uses an orthogonal one-dimensional failure space:

```math
\widehat{\mathcal R}(\sigma)
=\mathcal R(\sigma)\oplus
\mathrm{Tr}\!\left[(I-E_{\mathrm{succ}})\sigma\right]
|\mathrm{fail}\rangle\langle\mathrm{fail}|.
```

This is a trace-preserving channel. Keeping its outcome label gives the instrument viewpoint of Section 2.3.2.

### The exactness condition includes coherences

For $`\mathcal N_S=\mathrm{Tr}_{S^c}\circ\mathcal E`$, the successful logical map must obey

```math
\mathcal R_S\mathcal N_S=q_S\mathrm{id}_L
```

on the full operator space. Correct action on computational basis states alone is insufficient. For instance, qubit dephasing fixes both $`|0\rangle\langle0|`$ and $`|1\rangle\langle1|`$ but sends $`|0\rangle\langle1|`$ to zero.

Tensoring the channel equality with an identity map proves the reference statement directly:

```math
(\mathrm{id}_A\otimes\mathcal R_S\mathcal N_S)(\rho_{AL})
=q_S\rho_{AL}
```

for every joint state. The trace is $`q_S`$, and conditioning on success returns the original joint state. This is the meaning of preserving an unknown qubit, including its entanglement with systems unavailable to the decoder.

### Why every effective Kraus operator must be a scalar identity

For an isometric encoder $`V`$, choose a basis $`\{|e\rangle\}`$ of the erased systems. The composition of erasure with successful decoder Kraus operators $`R_a`$ has effective logical Kraus operators

```math
A_{a,e}=R_a(I_S\otimes\langle e|)V.
```

The Kraus index includes the erased environment. Amplitudes associated with different environment basis words are not added coherently after the partial trace.

The Choi representation gives a useful equivalence:

```math
\sum_{a,e}A_{a,e}(\,\cdot\,)A_{a,e}^\dagger
=q\mathrm{id}_L
\quad\Longleftrightarrow\quad
A_{a,e}=c_{a,e}I_L,\qquad
\sum_{a,e}|c_{a,e}|^2=q.
```

Here is the missing necessity argument. The Choi operator on the left is

```math
\sum_{a,e}
|\mathrm{vec}(A_{a,e})\rangle
\langle\mathrm{vec}(A_{a,e})|,
```

whereas the right side has support only on $`\mathrm{vec}(I_L)`$. For a vector $`w`$ orthogonal to that support,

```math
0=\sum_{a,e}
\left|\langle w,\mathrm{vec}(A_{a,e})\rangle\right|^2.
```

Every nonnegative term vanishes. Each vectorized Kraus operator therefore lies in the same one-dimensional subspace. The converse follows by substitution. If $`q=0`$, all effective Kraus operators are zero.

This is a derivation from the Choi formalism, not a separate numbered textbook theorem. It is the criterion implemented by the project's [exact verifier](../verification/verify_exact.py).

<a id="a-complete-filtering-example"></a>
## A complete filtering example

Consider a qubit and the two branch operators

```math
M_0=\frac12
\begin{pmatrix}\sqrt3&0\\0&1\end{pmatrix},
\qquad
M_1=\frac12
\begin{pmatrix}1&0\\0&\sqrt3\end{pmatrix}.
```

They satisfy $`M_0^\dagger M_0+M_1^\dagger M_1=I`$. Thus they define an instrument, or a coherent isometry

```math
U|\psi\rangle
=M_0|\psi\rangle\otimes|0\rangle_F
+M_1|\psi\rangle\otimes|1\rangle_F.
```

Measuring the flag gives

```math
\Pr(0\mid\rho)=\frac34\rho_{00}+\frac14\rho_{11}.
```

The branch probability depends on the input. The branch also changes superpositions: for $`|+\rangle`$, flag zero leaves the normalized state $`(\sqrt3|0\rangle+|1\rangle)/2`$.

Now condition the following filters on the measured flag:

```math
T_0=
\begin{pmatrix}1/\sqrt3&0\\0&1\end{pmatrix},
\qquad
T_1=
\begin{pmatrix}1&0\\0&1/\sqrt3\end{pmatrix}.
```

Both are contractions, so each is a valid successful operation. On the joint data-flag input, the decoder Kraus operators are $`T_s\otimes\langle s|`$. Their total effect is at most the identity, and the failure completion above supplies the remaining outcome.

The effective successful operators are

```math
T_0M_0=\frac12I,\qquad T_1M_1=\frac12I.
```

Writing $`\mathcal U(\rho)=U\rho U^\dagger`$, consequently,

```math
\mathcal R\mathcal U(\rho)
=\frac14\rho+\frac14\rho=\frac12\rho.
```

Each intermediate flag probability depends on $`\rho`$, but the final exact success probability is the constant $`1/2`$. The scalar-identity condition explains the distinction.

An input-independent lottery would choose a fixed probability before acting on the unknown state. Here, normalizing $`M_s\rho M_s^\dagger`$ requires division by an input-dependent trace; the normalized conditional transformation is not itself a linear encoding channel.

This example illustrates instrument bookkeeping, not an access advantage or an optimal decoder. If both outputs of the coherent isometry $`U`$ remain available, a joint decoder can invert it deterministically. The project's additional constraint is that three distributed carrier blocks have been erased.

<a id="coherent-flags-and-a-valid-encoder"></a>
## Coherent flags and a valid encoder

The [source construction](../science/construction.md#the-two-source-states) produces two orthogonal, unnormalized five-ququart vectors with

```math
\|f\|^2=20,\qquad
\|g\|^2=5(D-4),\qquad
\langle f|g\rangle=0.
```

Here $`f`$ has one defect level $`v`$, while $`g`$ has no defect. Within the strict-advantage interval $`0<x<1/4`$, one has $`D<8`$, so their norms differ.

The normalized vector

```math
|\psi\rangle_{AQ}
=\frac{|0\rangle_Af+|1\rangle_Ag}{\sqrt{5D}}
```

has reference marginal $`\mathrm{diag}(4/D,(D-4)/D)`$. The Choi normalization above requires $`I_A/2`$ for a qubit channel, so this vector alone is not the Choi vector of a trace-preserving encoder in that interval.

Let $`F_s=|s\rangle^{\otimes5}`$ and define

```math
V|0\rangle=\frac{fF_0+gF_1}{\sqrt{5D}},
\qquad
V|1\rangle=\frac{gF_0+fF_1}{\sqrt{5D}}.
```

Orthogonality of the flag strings removes cross terms within each norm, and $`f\perp g`$ removes the overlap between the two columns. Both columns have norm one because $`20+5(D-4)=5D`$. Thus $`V^\dagger V=I_2`$.

This is the isometric-channel case of Watrous's Corollary 2.27, with all output systems retained as physical carriers. The associated channel is $`\mathcal V(\rho)=V\rho V^\dagger`$. It is a deterministic encoder and requires no successful preparation event.

Write $`W_0|0\rangle=f`$, $`W_0|1\rangle=g`$. The two flag branches are $`M_0=W_0/\sqrt{5D}`$ and $`M_1=W_0X/\sqrt{5D}`$. Their effects sum to $`I_2`$, but neither is proportional to an isometry when $`D\ne8`$. Their probabilities have the same input-dependent structure as the toy example.

Erasing a nonempty complement removes flag coherence because

```math
\mathrm{Tr}_{S^c}
\bigl(|0\rangle^{\otimes5}\langle1|^{\otimes5}\bigr)=0.
```

The surviving pair can still read the flag and select its correction. Every flag resides in an erasable carrier. At the boundary values $`x=0,1/4`$, $`D=8`$ and the dephased branches instead have fixed probabilities $`1/2`$; those parameters do not give a strict advantage.

### Why separate normalization does not retain this advantage

The alternative isometry

```math
W|0\rangle=f/\sqrt{20},
\qquad
W|1\rangle=g/\sqrt{5(D-4)}
```

has optimal pair success exactly $`2/5`$ for $`0<x<1/4`$. The [component lemma](../science/interpretation.md#component-lemma) supplies the full proof. Its key upper-bound step now follows immediately from the scalar-identity criterion: if an erased environment word contains a defect, its logical-one column is zero because $`g`$ contains no defect. A scalar identity with a zero column must vanish. Every successful decoder therefore rejects all sectors where the defect lies outside the pair. Only $`2/5`$ of the logical-zero input mass remains.

The matching decoder applies the stated pair filter followed by $`\mathrm{diag}(1,\sqrt{(D-4)/4})`$. This is contractive for $`D<8`$ and gives four effective Kraus operators $`t^kI_2/\sqrt{10}`$, $`k=0,1,2,3`$, attaining $`2/5`$. This conclusion concerns these particular separately normalized source states, not all encoders without flags.

<a id="reading-the-pentagon-recovery-proof"></a>
## Reading the pentagon recovery proof

The [canonical proof](../science/recovery.md) has three logically distinct steps.

**First, the decoder must be physical on every pair input.** Stack the two ququart Kraus matrices $`K_0,K_1`$. Their four rows have disjoint supports and unit norm, so the stacked matrix $`K`$ obeys $`KK^\dagger=I_4`$. It follows that

```math
P=K^\dagger K,\qquad P^2=P,\qquad 0\le P\le I_{16}.
```

This proves trace nonincrease even for inputs outside the code. With pair flags, the successful operators are

```math
\widetilde K_{\ell,s}
=(X^sK_\ell)\otimes\langle ss|,
\qquad \ell,s\in\{0,1\}.
```

Unequal flags are rejected. The total effect is $`P\otimes(|00\rangle\langle00|+|11\rangle\langle11|)\le I_{64}`$.

**Second, the accepted environment must match for both logical components.** For the ordered pair $`(0,1)`$, with erased sites $`(2,3,4)`$, the amplitude identities give

```math
(K_\ell\otimes I)f=\sqrt2\,|0\rangle|E_\ell\rangle,
\qquad
(K_\ell\otimes I)g=\sqrt2\,|1\rangle|E_\ell\rangle,
```

where

```math
E_0=|111\rangle,\qquad
E_1=t|011\rangle+t^2|101\rangle+t^3|110\rangle.
```

The unwanted output amplitudes cancel before the environment is traced out. The desired outputs share the same $`E_\ell`$, which preserves their relative phase. Knowing only the two correct output populations would not establish this.

**Third, combine the flags and sum probabilities.** The conditional output $`X^s`$ cancels the logical exchange in the flag-$`s`$ source. There are four environment coefficients for each of two flag values:

```math
A_{s,k}=\frac{\sqrt2\,t^k}{\sqrt{5D}}I_2,
\qquad s=0,1,\quad k=0,1,2,3.
```

Since $`|t|=1`$, the scalar-identity criterion gives

```math
\mathcal R_i\mathrm{Tr}_{S_i^c}\mathcal V
=\left(8\frac2{5D}\right)\mathrm{id}_2
=\frac{16}{5D}\mathrm{id}_2.
```

Cyclic invariance supplies the same calculation for every ordered pair $`(i,i+1)`$, including $`(4,0)`$. The ordering matters because it specifies which tensor factor is the first input of $`K_\ell`$.

The eight Kraus operators describe distinct retained classical outcomes or erased environment words. Their probabilities add; their amplitudes do not combine into one coefficient. [Verification](../verification/README.md) makes that distinction explicit in exact number-field arithmetic for $`x=1/8`$.

<a id="the-arbitrary-code-benchmark"></a>
## The arbitrary-code benchmark

The benchmark is a convex hull of **binary operational profiles**. For each queried subset, a branch either recovers with certainty or deliberately aborts. An input-independent random variable selects the branch. Each branch may use an arbitrary quantum encoder with entangled code states and arbitrary finite carrier dimensions.

The restriction is on that branch's assigned recovery decisions, not on whether its physical encoder is quantum. A zero entry means abort; it does not assert secrecy or impossibility of recovery by a different decoder.

### The no-cloning step for arbitrary channels

Suppose two disjoint subsets $`S,T`$ have successful operations with logical maps $`q_S\mathrm{id}`$ and $`q_T\mathrm{id}`$. Their completed instruments can be applied jointly. Let $`\mathcal J`$ denote the CP map for both succeeding.

Each logical marginal of $`\mathcal J`$ is a CP submap of the corresponding single-success map. In Choi form, its positive operator is bounded above by a rank-one operator. The same support argument used earlier makes each marginal a scalar identity channel. The scalars agree because both marginal maps have the same trace. Write their common value as $`c`$.

If $`c>0`$, then $`\mathcal J/c`$ is a channel with two exact identity marginals. Apply it to half of $`|\Phi_K\rangle`$. The reference and first output have a pure maximally entangled joint state. A state with a pure marginal is a product with every other system: positivity confines its support to that one-dimensional marginal support. The reference and second output would therefore be uncorrelated, contradicting the second identity marginal for $`K>1`$. Hence $`c=0`$ and joint success is impossible.

This derivation does not assume an isometric encoder, pure ancillas, projective success effects, or a restricted decoder rank. It also gives $`q_S+q_T\le1`$, since the two success events are exclusive in their joint instrument.

### From disjointness to the classical score

In a binary profile, two successful queried subsets must therefore intersect. For the five cycle edges, at most two can be pairwise intersecting. For example, once $`\{0,1\}`$ succeeds, the only other edges meeting it are $`\{1,2\}`$ and $`\{4,0\}`$, and those two are disjoint.

Every binary branch obeys $`\sum_i b_i\le2`$. Taking an input-independent convex mixture preserves that linear inequality:

```math
q_i=\sum_\lambda w_\lambda b_i^{(\lambda)}
\quad\Longrightarrow\quad
\sum_iq_i\le2.
```

The value is attainable by choosing a carrier uniformly and storing the qubit there; its two incident edges recover deterministically. Thus the optimal uniform-query average within this benchmark is $`2/5`$.

Routing proves attainability, while the preceding converse covers arbitrary quantum codes. Pairwise probabilistic inequalities alone would allow a larger total score, so they do not contradict the project's value slightly above two. [Access profiles](../science/access_profiles.md#the-pentagon-bound-is-exactly-two) gives the full benchmark statement and its graph formulation.

<a id="why-five-carriers-are-minimal"></a>
## Why five carriers are minimal

No-cloning and the pentagon calculation establish the five-carrier separation. They do not by themselves exclude every possible query family on fewer carriers.

That additional input is the constructive classification for $`n\le4`$ in [Alhejji et al., *Constraints on recovering quantum information after erasure*](https://arxiv.org/html/2607.17319v2), discussed in [Related work](../references/RELATED_WORK.md#alhejji2026). Its small-carrier constructions start with binary access profiles and use carrier permutations, unused carriers, reductions of coordinates, and convex mixing.

To connect that result to this project's benchmark, each operation must preserve the binary-profile convex hull. Relabeling and adding unused carriers preserve binary profiles. Mixing is built into the definition. For a coordinate reduction, presample an acceptance coin for every query and abort when its coin rejects. Conditioned on all coins and the original binary branch, the result is again a binary subprofile. Averaging realizes any coordinatewise reduction.

Consequently, every attainable complete profile on at most four carriers belongs to the benchmark. Restricting a profile to any smaller query family preserves its convex representation. The explicit five-carrier violation supplies the other direction, establishing minimality in the model with finite but unrestricted carrier dimensions. The detailed dependency is in [Five-carrier minimality](../science/access_profiles.md#five-carrier-minimality).

The count is of carrier blocks. It does not establish the minimum number of physical qubits, and it does not assume statistically independent erasures.

<a id="resources-and-claim-boundaries"></a>
## Resources and claim boundaries

The uniform construction uses $`B_j=Q_j\otimes\mathsf F_j`$, where $`\dim Q_j=4`$ and $`\dim\mathsf F_j=2`$. These are five dimension-eight carriers, equivalently five blocks of three qubits. Erasure removes an entire block, including its flag. The decoder has joint access to the surviving pair and knows its label. No retained sender system or noiseless quantum side channel supplies missing information.

The [resource discussion](../science/interpretation.md#5-resource-accounting) also describes a version with local dimensions $`(8,4,8,4,8)`$. Neither version establishes minimal local dimension, a circuit-depth bound, a fault-tolerance threshold, or decoding by local operations and classical communication alone.

### Attained score, family optimum, and global bound

For the explicit family,

```math
D(x)=5-4x+\frac3{1-x},
\qquad 0\le x\le\frac34,
\qquad Q(x)=\frac{16}{D(x)}.
```

Putting $`y=1-x`$ gives the elementary optimization

```math
D-(1+4\sqrt3)
=\frac{(2y-\sqrt3)^2}{y}\ge0.
```

The allowed value $`y=\sqrt3/2`$ attains equality. The [parameter-family proof](../science/parameter_family.md#exact-family-optimum) therefore establishes

```math
Q_{\mathrm{family}}^{\max}
=\frac{16}{1+4\sqrt3}>2,
\qquad
q_i=\frac{Q_{\mathrm{family}}^{\max}}5.
```

The optimum is over the displayed parameter and decoder family. It is not an upper bound on another decoder for the same encoder or on another encoder. Alhejji et al.'s universal pentagon bound instead yields

```math
\frac{16}{1+4\sqrt3}
\le Q_{\mathrm{best}}\le\sqrt5,
```

where the optimization permits arbitrary finite carrier dimensions. The [canonical statement](../science/model.md#main-theorem) keeps these distinct claims separate.

Finally, the five queried pairs are alternatives under a specified correlated erasure distribution. Each carrier survives with marginal probability $`2/5`$, but the survivors are restricted to adjacent pairs. A result for these five queries is not a guarantee for all ten pairs or for independent erasures. The channel, source construction, and comparison must all use this same resource model.
