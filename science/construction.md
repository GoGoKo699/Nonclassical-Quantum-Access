# A cyclic code with coherent flags

The encoder combines two sparse states on five four-level systems. One state contains a single distinguished defect; the other contains only background levels. Their amplitudes are chosen so that a two-site filter can erase all false logical outcomes and match the two correct logical amplitudes. A binary flag inside each carrier turns these two states into a valid isometric code.

The model and main statement are in [Exact recovery after a pair survives](model.md). The decoder is proved in [Recovery](recovery.md).

## One parameter

Choose a real parameter

```math
0\le x\le\frac34
```

and define

```math
t=x+i\sqrt{1-x^2},\qquad
\beta_2=\frac{2t^2}{1-t},\qquad
\beta_1=(2x-1)\beta_2,
```

```math
\gamma=\sqrt{1-\frac{|\beta_1|^2}{2}},\qquad
D=4+|\beta_1|^2+|\beta_2|^2+\gamma^2.
\tag{1}
```

The nonnegative root defines $`\gamma`$. The conjugate choice of $`t`$ gives the same success probability. Since $`|t|=1`$ and $`x\le3/4`$, the denominator $`1-t`$ is nonzero.

The identities

```math
t+t^{-1}=2x,\qquad
|\beta_2|^2=\frac2{1-x},\qquad
|\beta_1|^2=\frac{2(2x-1)^2}{1-x}
\tag{2}
```

give

```math
\gamma^2=\frac{x(3-4x)}{1-x}\ge0.
\tag{3}
```

Thus every value in the stated interval defines a physical construction. The attainable score and its exact optimum are derived in [Parameter family](parameter_family.md).

## The two source states

Each four-level system has the orthonormal basis

```math
\{|v\rangle,|0\rangle,|1\rangle,|2\rangle\}.
```

The symbol $`v`$ denotes a distinguished defect level; the digits denote three background levels. All site labels below are modulo five. The notation $`|v_j,0_k,1_{\mathrm{rest}}\rangle`$ means the computational-basis word with a defect at $`j`$, background zero at $`k`$, and background one elsewhere.

Define the unnormalized states

```math
|f\rangle=
\sum_{j=0}^4\sum_{k=1}^4
t^{k-1}|v_j,0_{j+k},1_{\mathrm{rest}}\rangle
\tag{4}
```

and

```math
\begin{aligned}
|g\rangle=\sum_{j=0}^4\bigl[
&\beta_1|0_j,0_{j+1},1_{\mathrm{rest}}\rangle\\
&+\beta_2|0_j,0_{j+2},1_{\mathrm{rest}}\rangle\\
&+\gamma|2_j,1_{\mathrm{rest}}\rangle
\bigr].
\end{aligned}
\tag{5}
```

There are twenty distinct words in $`f`$: five possible defect positions and four possible zero positions relative to it. The three orbits in $`g`$ each contain five distinct words. The adjacent-zero, nonadjacent-zero, and single-two orbits are mutually disjoint.

The norms follow by summing squared amplitudes:

```math
\langle f|f\rangle=20,\qquad
\langle g|g\rangle
=5\bigl(|\beta_1|^2+|\beta_2|^2+\gamma^2\bigr)
=5(D-4).
\tag{6}
```

Moreover,

```math
\langle f|g\rangle=0,
\tag{7}
```

because every word of $`f`$ contains a defect and no word of $`g`$ does. At a boundary value where an orbit coefficient vanishes, its terms simply disappear; the norm identities remain valid.

Let $`P`$ shift each site to the next site. Relabeling $`j`$ in (4) and (5) shows

```math
P|f\rangle=|f\rangle,\qquad
P|g\rangle=|g\rangle.
\tag{8}
```

This exact cyclic invariance is why one decoder can serve all five ordered pairs without any pair-dependent phase correction.

## The physical encoder

Attach one flag qubit to each four-level system. Each physical carrier is

```math
B_j=Q_j\otimes\mathsf F_j\simeq\mathbb C^4\otimes\mathbb C^2
\simeq\mathbb C^8.
```

Write $`F_0=|0\rangle^{\otimes5}`$ and $`F_1=|1\rangle^{\otimes5}`$ for the two uniform flag strings. Products such as $`fF_0`$ are regrouped site by site into the five physical carriers $`Q_j\mathsf F_j`$.

Define

```math
\boxed{
\begin{aligned}
V|0\rangle&=
\frac{|f\rangle F_0+|g\rangle F_1}{\sqrt{5D}},\\
V|1\rangle&=
\frac{|g\rangle F_0+|f\rangle F_1}{\sqrt{5D}}.
\end{aligned}}
\tag{9}
```

Each column has squared norm

```math
\frac{\|f\|^2+\|g\|^2}{5D}=1.
```

Their inner product vanishes by (7) and the orthogonality of $`F_0,F_1`$. Hence

```math
V^\dagger V=I_2.
\tag{10}
```

Equation (9) is therefore a deterministic isometric encoder into precisely five dimension-eight carriers. It has no inaccessible encoding environment. The flags are part of the physical code and are erased with their carriers.

## Why the flag is coherent

Let $`W_0`$ be the unnormalized source map defined by

```math
W_0|0\rangle=|f\rangle,\qquad
W_0|1\rangle=|g\rangle.
```

The two flag branches in (9) are

```math
M_0=\frac{W_0}{\sqrt{5D}},\qquad
M_1=\frac{W_0X}{\sqrt{5D}},
\qquad
M_0^\dagger M_0+M_1^\dagger M_1=I_2.
\tag{11}
```

Neither branch is separately trace preserving. For an input $`\rho`$, the probability of flag zero after its measurement is

```math
\Pr(0\mid\rho)
=\frac4D\,\rho_{00}
+\frac{D-4}{D}\,\rho_{11}.
\tag{12}
```

When $`D\ne8`$, it depends on the logical input. In particular, throughout the strict-advantage interval $`0<x<1/4`$, the displayed branches cannot be interpreted as an input-independent classical lottery between encoding channels. They form a coherent implementation of a complete instrument. At $`x=0`$ and $`x=1/4`$, one has $`D=8`$; each branch then occurs with probability $`1/2`$ and is proportional to an isometry. After dephasing the flag, those boundary cases do admit the fixed-lottery interpretation.

After erasure of any nonempty complement, the two uniform flag strings become incoherent in the surviving system because their erased parts are orthogonal. A surviving pair reads its flag value, applies the pair decoder, and corrects by $`X`$ for flag one. [Recovery](recovery.md) proves that the final successful logical map is nevertheless a constant times the identity.

## Reference-state formulation

For completeness, introduce the normalized source

```math
|\psi\rangle_{AQ}
=\frac{|0\rangle_A|f\rangle+|1\rangle_A|g\rangle}{\sqrt{5D}}.
```

Its reference marginal is

```math
\rho_A=
\operatorname{diag}\!\left(\frac4D,\frac{D-4}{D}\right).
\tag{13}
```

This biased source is a convenient algebraic device. The normalized Choi vector of the physical encoder (9) is instead

```math
|\Psi\rangle
=\frac{|\psi\rangle F_0+X_A|\psi\rangle F_1}{\sqrt2}.
\tag{14}
```

Its reference marginal is exactly $`I_2/2`$, as is also guaranteed by (10). The source-vector calculation and the physical isometry are therefore distinct steps, with no implicit input postselection.

The [interpretation](interpretation.md) explains the role of this balancing through a comparison with a separately normalized unflagged code.
