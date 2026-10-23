# Physical interpretation and resources

The construction preserves a qubit through a specified correlated-erasure event: one adjacent pair of a five-carrier cycle survives, and the other three carriers are erased. Every surviving pair can return the input **exactly**, with the same heralded success probability. For a uniformly chosen adjacent pair, this probability exceeds the optimal average $`2/5`$ of any input-independent classical lottery over binary exact-access protocols.

For the rational example, each pair succeeds with probability $`224/555`$. The best member of the displayed parameter family gives

```math
p_{\mathrm{succ}}=\frac{16}{5(1+4\sqrt3)}
\approx0.4036223476>\frac25.
```

The improvement is small in magnitude. Its significance is a strict separation between realizable quantum recovery probabilities and mixtures of deterministic access decisions. The comparison permits arbitrary quantum codes in each lottery branch; it is not limited to routing a qubit to one site. See the [operational model](model.md) and [access-profile comparison](access_profiles.md).

The canonical construction is translation invariant: the same two-site filter is used on every ordered adjacent pair, including $`(4,0)`$. The full encoded states are in [construction.md](construction.md), and the exact channel identities are proved in [recovery.md](recovery.md).

## 1. The filter matches amplitudes and cancels false outcomes

The four-level part of each carrier has basis $`\{v,0,1,2\}`$. The unnormalized source word $`f`$ contains one distinguished defect $`v`$, one background zero, and three background ones. Its defect is uniformly distributed over the five sites. The second word $`g`$ has no defect: it combines configurations with two background zeros and configurations with a single background two.

The successful two-site filter has two functions:

1. When the defect lies inside the surviving pair, it coherently combines its two possible positions.
2. When the defect lies outside, the two possible positions of the background zero inside the pair cancel in the unwanted logical output.

The cancellation is the elementary relation

```math
d\,t^{k-1}+e\,t^k=0,
\qquad d=-\frac{t}{\sqrt2},\quad e=\frac1{\sqrt2}.
```

The amplitudes in $`g`$ are chosen to match the accepted amplitudes from $`f`$. For either logical component, the four surviving erased-environment configurations have amplitudes

```math
\sqrt2,\qquad \sqrt2t,\qquad \sqrt2t^2,\qquad \sqrt2t^3,
\qquad |t|=1.
```

Thus a successful branch leaves the same environment state for both logical basis components. The environment carries no information distinguishing those components within that branch, and their relative phase is preserved. This amplitude matching establishes recovery of arbitrary superpositions, not merely correct outputs on the two basis states.

## 2. The flag balances unequal source weights

The two source words are orthogonal but have different norms:

```math
\langle f|g\rangle=0,\qquad
\|f\|^2=20,\qquad
\|g\|^2=5(D-4).
```

Throughout the strict-advantage interval of the [parameter family](parameter_family.md), $`0<x<1/4`$ and $`D<8`$. The defect component therefore has greater norm. The normalized reference-source state

```math
|\psi\rangle=
\frac{|0\rangle_A|f\rangle+|1\rangle_A|g\rangle}{\sqrt{5D}}
```

has reference marginal $`\mathrm{diag}(4/D,(D-4)/D)`$. It is not by itself the Choi vector of a trace-preserving encoding of an arbitrary qubit.

Attach a flag qubit to every carrier and let $`F_s=|s\rangle^{\otimes5}`$. The isometric encoder is

```math
V|0\rangle=\frac{fF_0+gF_1}{\sqrt{5D}},
\qquad
V|1\rangle=\frac{gF_0+fF_1}{\sqrt{5D}}.
```

Both columns have unit norm, and their inner product is zero. The two flag branches exchange the unequal source weights without changing the relative amplitudes needed by the recovery filter.

After erasure, the surviving pair reads a flag. For flag zero it uses the original filter. For flag one it uses that filter and then applies $`X`$ to the recovered qubit. Unequal surviving flag values are rejected; they do not occur on encoded inputs. The erased flags distinguish the two branches. All flags belong to the erasable physical carriers; none is retained by the sender.

### Input-dependent branch weights are not a classical code lottery

Write the two unflagged branch maps as

```math
M_0=\frac{|f\rangle\langle0|+|g\rangle\langle1|}{\sqrt{5D}},
\qquad
M_1=\frac{|g\rangle\langle0|+|f\rangle\langle1|}{\sqrt{5D}}.
```

They obey

```math
M_0^\dagger M_0=
\begin{pmatrix}4/D&0\\0&(D-4)/D\end{pmatrix},
\qquad
M_1^\dagger M_1=I-M_0^\dagger M_0.
```

For an input state $`\rho`$, the probability of reading flag zero is

```math
\Pr(0\mid\rho)=\frac{4\rho_{00}+(D-4)\rho_{11}}{D}.
```

The flag therefore labels a weak filtering branch whose probability depends on the unknown input. An input-independent lottery over encoding channels would instead choose its branch with a fixed probability before the input was processed. Neither $`M_s`$ is a constant multiple of an isometry when $`D\ne8`$, so these two descriptions are different physical operations.

This intermediate input dependence does **not** make the advertised recovery probability input dependent. Once the successful filter and conditional $`X`$ are included, each flag branch contributes $`8/(5D)`$ times the identity channel. Together they give

```math
\mathcal R_i\circ\mathrm{tr}_{S_i^c}\circ\mathcal V
=\frac{16}{5D}\mathrm{id}_2.
```

The coherent flag construction gives a pure isometric implementation. If mixed encoders are allowed, the two maps $`M_0,M_1`$ can instead be implemented as a quantum instrument with a copied outcome flag. Its input-dependent filtering still differs from an input-independent lottery over deterministic-access protocols.

## 3. What separate normalization loses

The following component lemma makes the flag's role precise for these particular source states. It does not assert that every code with an advantage must use flags.

### Component lemma

For $`0<x<1/4`$, define the unflagged isometric encoder

```math
W|0\rangle=\frac{f}{\sqrt{20}},
\qquad
W|1\rangle=\frac{g}{\sqrt{5(D-4)}}.
```

For each adjacent pair, its optimal probability of exact conclusive identity recovery, over all trace-nonincreasing recovery maps, is exactly $`2/5`$.

**Upper bound.** Let $`R_a`$ be arbitrary successful recovery Kraus operators on a pair $`S`$, and choose a computational basis $`\{|e\rangle\}`$ for the erased complement. The effective logical Kraus operators are

```math
A_{a,e}=R_a(I_S\otimes\langle e|)W.
```

If the successful logical channel equals $`q\mathrm{id}_2`$, its Choi matrix has rank one. It is a sum of positive outer products of the vectorized $`A_{a,e}`$, so every effective Kraus operator must individually be proportional to $`I_2`$.

If the erased word $`e`$ contains a defect, the logical-one column of $`A_{a,e}`$ is zero: $`g`$ has no defect anywhere. A scalar identity with a zero column is zero. Hence every sector with the defect outside the surviving pair must be rejected exactly.

For the input $`|0\rangle`$, the defect in $`f/\sqrt{20}`$ lies inside a given pair with probability $`2/5`$. Trace nonincrease prevents a successful decoder from accepting more than this remaining mass. Therefore $`q\le2/5`$, irrespective of recovery Kraus rank or independent local recovery ancillas.

**Attainment.** Apply the same two-site filter as in the construction, then attenuate its logical-one output by

```math
A=\mathrm{diag}\left(1,\sqrt{\frac{D-4}{4}}\right).
```

The stated parameter interval gives $`D<8`$, so this attenuation is contractive. It makes the two accepted logical amplitudes equal because

```math
\frac{\sqrt2}{\sqrt{20}}
=\sqrt{\frac{D-4}{4}}\frac{\sqrt2}{\sqrt{5(D-4)}}
=\frac1{\sqrt{10}}.
```

The four nonzero effective Kraus operators are then $`I_2,tI_2,t^2I_2,t^3I_2`$, each divided by $`\sqrt{10}`$. Their squared coefficients sum to $`2/5`$, attaining the upper bound.

Separate normalization thus produces a valid encoder with optimal pair success exactly $`2/5`$. The flag construction preserves the source's favorable unequal weights while completing them to a valid isometry, giving success strictly above $`2/5`$.

## 4. Equivalent GHZ-phase form

There is another useful expression for the same encoder. Continue within the strict-advantage interval $`0<x<1/4`$ and define

```math
m_\pm=\frac{f\pm g}{\sqrt{5D}},
\qquad
|\mathrm{GHZ}_\pm\rangle=\frac{F_0\pm F_1}{\sqrt2}.
```

Both $`m_\pm`$ are normalized, and

```math
V|\pm\rangle=m_\pm\otimes|\mathrm{GHZ}_\pm\rangle,
\qquad
\langle m_+|m_-\rangle=\delta:=\frac{8-D}{D}>0.
```

In this logical basis the ququart words are slightly nonorthogonal, while the opposite GHZ phases make the complete encoded words orthogonal. Within this construction, the total success has the simple relation

```math
Q=\frac{16}{D}=2+2\delta.
```

For the rational member, $`D=111/14`$ and $`\delta=1/111`$. Thus $`Q=2+2/111`$. This identity describes this parameter family; it is not a general formula for the recovery probability of arbitrary pairs of nonorthogonal codewords.

## 5. Resource accounting

| Resource | Specification |
|---|---|
| Logical input | One arbitrary qubit, possibly entangled with an external reference |
| Erasable carriers | Five, labeled on a cycle |
| Uniform local dimension | $`8=4\times2`$: a ququart and one flag qubit per carrier |
| Equivalent qubit grouping | Fifteen physical qubits in five three-qubit carrier blocks; erasure removes a whole block |
| Surviving query | One of the five ordered adjacent pairs; the decoder knows which pair survived |
| Recovery | A joint quantum operation on the two survivors, with a success/failure outcome |
| Erased systems | The other three complete carriers, including their flags |
| External assistance | No retained sender system, noiseless side channel, feedback, or preshared sender–receiver entanglement |
| Circuit claim | A finite encoder and recovery map are specified; no gate-depth or fault-tolerance claim is made |

The decoder is allowed a **joint** operation on the surviving pair. This is not a guarantee that two separated holders can decode using only local operations and classical communication.

An optional resource reduction stores copied flags only at the vertex cover $`\{0,2,4\}`$. Every queried adjacent pair then contains a flag, and every erased complement contains at least one flag. The same encoding and recovery argument works with local dimensions

```math
(8,4,8,4,8),
```

equivalent to thirteen physical qubits in five carriers. The uniform dimension-eight version keeps the cyclic symmetry explicit. Neither resource count is claimed minimal.

## 6. The correlated-erasure channel

For uniform carrier dimension, define a channel that transmits a uniformly chosen adjacent pair and reports its label:

```math
\mathcal N_{C_5}(\sigma)
=\frac15\sum_{i=0}^4|i\rangle\langle i|_C
\otimes\mathrm{tr}_{S_i^c}\sigma.
```

Each individual carrier survives with probability $`2/5`$, but the survival events are correlated. Composing this channel with the encoder and pair-conditioned recovery implements a logical erasure channel with transmission probability $`16/(5D)`$: on success the qubit is unchanged, and on failure its output may be replaced by an orthogonal erasure flag.

The physical channel has an explicit antidegrading map. Its environment can hold the complementary triple and a copy of the pair label $`i`$. Within that triple are exactly two cycle edges disjoint from $`S_i`$. The environment chooses either with probability $`1/2`$, discards the remaining carrier, and outputs the chosen edge with its own label. Every target edge is reached from two original labels, giving total probability $`2(1/5)(1/2)=1/5`$ and exactly the required quantum marginal. This reconstructs $`\mathcal N_{C_5}`$ from its complementary output for arbitrary inputs, including entangled inputs.

The operational comparison here concerns exact heralded recovery for this specified correlated channel. The [related-work discussion](../references/RELATED_WORK.md) distinguishes it from independent-erasure channel simulation and other quantum communication tasks.

## 7. Scope of the separation

The construction establishes a strict advantage over the convex hull of binary exact-recovery profiles for the five specified queries. It does not require the displayed decoder to be globally optimal for its encoder: any larger optimal recovery probabilities would retain the separation.

The guarantee concerns exact **conclusive** recovery. It does not give deterministic recovery after three erasures, a guarantee for all ten possible surviving pairs, an optimal local dimension, or a threshold under repeated noisy error correction. The extremum proved in [parameter_family.md](parameter_family.md) is within the displayed family, not over all possible pentagon encoders.

Only one surviving-pair query is performed in a transmission. Disjoint-pair instruments can nevertheless be applied jointly when establishing no-cloning constraints; for the construction their joint-success probability vanishes on the code. The associated pentagon and its contextuality interpretation are discussed in [access_profiles.md](access_profiles.md). The recovery-profile separation itself is an operational statement about quantum channels and classical mixtures and does not depend on adopting an ontological model.
