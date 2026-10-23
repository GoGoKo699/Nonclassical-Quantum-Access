# The exact pair recovery channel

This page proves the channel identity for the [cyclic flagged code](construction.md). The proof uses a short list of amplitudes and establishes recovery for every logical input. Numerical agreement with a Bell state is not an assumption of the argument.

Use the source states $`f,g`$, parameters $`t,\beta_1,\beta_2,\gamma,D`$, and isometry $`V`$ defined in [Construction](construction.md). First consider the ordered pair $`(0,1)`$, with erased sites ordered as $`(2,3,4)`$.

## Two successful Kraus operators

On the pair of four-level systems define

```math
\begin{aligned}
K_0=\frac1{\sqrt2}\bigl[
&|0\rangle(\langle v0|+t^{-3}\langle0v|)\\
&+|1\rangle(\overline{\beta_1}\langle00|
+\gamma\langle12|+\gamma\langle21|)
\bigr],
\end{aligned}
\tag{1}
```

```math
\begin{gathered}
K_1=\frac1{\sqrt2}\bigl[
|0\rangle(\langle v1|+t\langle1v|)
+|1\rangle(-t\langle01|+\langle10|)
\bigr].
\end{gathered}
\tag{2}
```

All unlisted matrix elements vanish. The output is one logical qubit. The four rows obtained by stacking $`K_0,K_1`$ have mutually disjoint supports in the pair basis. Three have norm one from $`|t|=1`$; the fourth has norm one because

```math
\frac{|\beta_1|^2+2\gamma^2}{2}=1.
```

Thus the stacked matrix is a coisometry. In particular,

```math
P=K_0^\dagger K_0+K_1^\dagger K_1
```

is an orthogonal projector of rank four, and $`P\le I_{16}`$. The successful operation

```math
\mathcal K(\tau)=\sum_{\ell=0}^1K_\ell\tau K_\ell^\dagger
```

is therefore completely positive and trace-nonincreasing on the entire two-ququart Hilbert space.

## Three identities that match the logical amplitudes

The definitions imply

```math
\begin{aligned}
\beta_1-t\beta_2
&=(t^{-1}-1)\beta_2=2t,\\
(1-t)\beta_2&=2t^2,\\
\beta_2-t\beta_1
&=(t-t^2)\beta_2=2t^3.
\end{aligned}
\tag{3}
```

The first and last equalities use $`t+t^{-1}=2x`$ and $`\beta_1=(2x-1)\beta_2`$. These identities hold throughout the parameter interval and do not require optimizing $`x`$.

## Exhaustive source-state calculation

The following table lists all nonzero correct logical outputs before source normalization. An erased word uses the background digits at sites $`(2,3,4)`$.

| Kraus label | Erased word | Amplitude from $`f`$, output zero | Amplitude from $`g`$, output one |
|---|---|---|---|
| $`0`$ | $`111`$ | $`(1+t^{-3}t^3)/\sqrt2=\sqrt2`$ | $`(\lvert\beta_1\rvert^2+2\gamma^2)/\sqrt2=\sqrt2`$ |
| $`1`$ | $`011`$ | $`(t+t)/\sqrt2=\sqrt2t`$ | $`(\beta_1-t\beta_2)/\sqrt2=\sqrt2t`$ |
| $`1`$ | $`101`$ | $`(t^2+t^2)/\sqrt2=\sqrt2t^2`$ | $`(1-t)\beta_2/\sqrt2=\sqrt2t^2`$ |
| $`1`$ | $`110`$ | $`(t^3+t^3)/\sqrt2=\sqrt2t^3`$ | $`(\beta_2-t\beta_1)/\sqrt2=\sqrt2t^3`$ |

The two columns agree by the row normalization and (3).

There are two possible types of incorrect logical output. A zero output from $`g`$ is excluded by support: both zero-output rows require a defect, and $`g`$ has none. A one output from $`f`$ can only arise from $`K_1`$, with the defect outside the surviving pair and the unique zero at one of its endpoints.

For an outside defect at $`j\in\{2,3,4\}`$, those two contributions are

```math
\begin{gathered}
\frac{-t\,t^{4-j}+t^{5-j}}{\sqrt2}=0.
\end{gathered}
\tag{4}
```

They have the same erased word and cancel coherently. The one-output row of $`K_0`$ cannot act on $`f`$, because it requires either two zeros or a background two.

Define the erased-system vectors

```math
\begin{gathered}
|E_0\rangle=|111\rangle,\qquad
|E_1\rangle=t|011\rangle+t^2|101\rangle+t^3|110\rangle.
\end{gathered}
\tag{5}
```

Their squared norms are $`1`$ and $`3`$. The table and cancellation give the exact vector identities

```math
\begin{aligned}
(K_\ell\otimes I)|f\rangle
&=\sqrt2\,|0\rangle|E_\ell\rangle,\\
(K_\ell\otimes I)|g\rangle
&=\sqrt2\,|1\rangle|E_\ell\rangle,
\qquad \ell=0,1.
\end{aligned}
\tag{6}
```

Equation (6) is the central recovery relation. The erased system has the same state for the two logical amplitudes in each accepted branch, so it retains no which-logical-state information in that branch.

## Recovery with the physical flags

Group the two ququart inputs before their two flags for the following formula. For $`s\in\{0,1\}`$, define the successful physical Kraus operators

```math
\begin{gathered}
\widetilde K_{\ell,s}
=(X^sK_\ell)\otimes\langle ss|.
\end{gathered}
\tag{7}
```

The pair reads equal flag values, applies $`K_\ell`$, and flips the recovered logical qubit for flag one. **Unequal surviving flags are rejected.** This specifies the decoder on the full pair Hilbert space, including states outside the code.

The success effect is

```math
\begin{gathered}
\widetilde P
=P\otimes
\bigl(|00\rangle\langle00|+|11\rangle\langle11|\bigr)
\le I_{64}.
\end{gathered}
\tag{8}
```

It is a rank-eight projector. A failure map

```math
\tau\longmapsto
\mathrm{Tr}\bigl[(I_{64}-\widetilde P)\tau\bigr]\,
|\mathrm{fail}\rangle\langle\mathrm{fail}|
```

completes the instrument when the failure flag is orthogonal to the successful logical output.

Write the unnormalized source map as $`W_0|0\rangle=f`$ and $`W_0|1\rangle=g`$. In the flag-$`s`$ branch of the encoder, the source map is $`W_0X^s/\sqrt{5D}`$. Equation (6) gives

```math
\begin{gathered}
(X^sK_\ell\otimes I)
\frac{W_0X^s}{\sqrt{5D}}
=\frac{\sqrt2}{\sqrt{5D}}\,
I_2\otimes|E_\ell\rangle.
\end{gathered}
\tag{9}
```

The remaining erased flags are orthogonal for the two values of $`s`$. Hence the complete effective logical Kraus operators are

```math
\begin{gathered}
\frac{\sqrt2}{\sqrt{5D}}I_2,\quad
\frac{\sqrt2t}{\sqrt{5D}}I_2,\quad
\frac{\sqrt2t^2}{\sqrt{5D}}I_2,\quad
\frac{\sqrt2t^3}{\sqrt{5D}}I_2,
\end{gathered}
\tag{10}
```

once for each flag value. There are eight nonzero effective Kraus operators. Summing their contributions proves

```math
\begin{gathered}
\boxed{
\mathcal R_0\circ\mathrm{Tr}_{234}\circ\mathcal V
=\frac{16}{5D}\mathrm{id}_2.
}
\end{gathered}
\tag{11}
```

The scalar-identity form in (10) proves the channel equality for arbitrary operators and entangled inputs. Exactness does not rely on a numerical fidelity threshold.

## All five pairs

Both source states and both uniform flag strings are cyclically invariant. Relabeling the pair $`(i,i+1)`$ as $`(0,1)`$ therefore changes only the ordering of the erased systems in (6) and (9). That ordering is traced out.

The same matrices (1), (2), and (7) consequently satisfy

```math
\begin{gathered}
\mathcal R_i\circ\mathrm{Tr}_{S_i^c}\circ\mathcal V
=\frac{16}{5D}\mathrm{id}_2,
\qquad i=0,1,2,3,4.
\end{gathered}
\tag{12}
```

No pair-dependent logical rotation is required. The ordered wraparound convention $`(4,0)`$ remains part of the definition.

## Joint success and no-cloning

Extend each success projector (8) to all five carriers, calling it $`\Pi_i`$. If the queried pairs are disjoint, $`\Pi_i`$ and $`\Pi_j`$ commute. Exact universal recovery implies

```math
\begin{gathered}
\Pi_i\Pi_jV=0
\qquad(S_i\cap S_j=\varnothing).
\end{gathered}
\tag{13}
```

Otherwise the two local recovery instruments would have a nonzero simultaneous success branch yielding two copies of an arbitrary logical state. The rank-one-Choi version of this argument is given in [Access profiles](access_profiles.md).

For the rational member $`x=1/8`$, the [exact certificate](../verification/verify_exact.py) directly verifies (12) and (13) in rational number-field arithmetic. The [family verifier](../verification/verify_family.py) separately checks the scalar identities and reconstructs the full dimension-eight encoder for numerical diagnostics. The written argument above supplies the exact theorem for every parameter in the stated interval.
