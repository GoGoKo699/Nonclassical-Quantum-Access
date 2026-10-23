# The attainable family and its optimum

The [construction](construction.md) and [recovery proof](recovery.md) provide an explicit encoder-decoder pair for every $`0\le x\le3/4`$. Each adjacent pair has success probability

```math
p(x)=\frac{16}{5D(x)},\qquad Q(x)=5p(x)=\frac{16}{D(x)}.
\tag{1}
```

This page evaluates that family exactly. Optimizing its parameter does not optimize over all possible codes, or over all possible decoders for the displayed encoder.

## A one-variable normalization

Using $`\gamma^2=1-|\beta_1|^2/2`$ gives

```math
\begin{aligned}
D(x)
&=5+\frac{|\beta_1|^2}{2}+|\beta_2|^2\\
&=5+\frac{(2x-1)^2+2}{1-x}\\
&=5-4x+\frac3{1-x}.
\end{aligned}
\tag{2}
```

Set $`y=1-x`$, so $`1/4\le y\le1`$. Then

```math
D=1+4y+\frac3y.
\tag{3}
```

The two variable terms represent the normalization cost required to match all four successful logical amplitudes.

## Exact family optimum

For $`y>0`$,

```math
D-(1+4\sqrt3)
=\frac{(2y-\sqrt3)^2}{y}\ge0.
\tag{4}
```

Equality holds at $`y=\sqrt3/2`$, which lies inside the allowed interval. Thus the specified family attains its largest score at

```math
x_{\mathrm{opt}}=1-\frac{\sqrt3}{2},
\qquad
D_{\min}=1+4\sqrt3,
```

```math
\boxed{
p_{\mathrm{fam}}^{\max}
=\frac{16}{5(1+4\sqrt3)}
=0.403622347593226\ldots,
}
\tag{5}
```

```math
Q_{\mathrm{fam}}^{\max}
=\frac{16}{1+4\sqrt3}
=2.018111737966131\ldots.
\tag{6}
```

The strict separation from the deterministic-mixture score two follows from

```math
1+4\sqrt3<8,
```

because $`48<49`$. No numerical optimization is needed.

At this parameter,

```math
|\beta_1|^2=\frac{16}{\sqrt3}-8,\qquad
|\beta_2|^2=\frac4{\sqrt3},\qquad
\gamma^2=5-\frac8{\sqrt3}.
```

All of these are compatible with the normalized decoder rows. In particular, $`\gamma^2>0`$ follows from $`75>64`$.

## The entire strict-advantage interval

Subtracting the deterministic-mixture normalization threshold gives

```math
D(x)-8=\frac{x(4x-1)}{1-x}.
\tag{7}
```

Since the denominator is positive, the displayed family obeys

```math
Q(x)>2
\quad\Longleftrightarrow\quad
0<x<\frac14.
\tag{8}
```

At $`x=0`$ and $`x=1/4`$, the score equals two. For $`1/4<x\le3/4`$, the same construction remains a valid exact recovery code but its displayed score is below two.

Equation (8) gives a continuous family of exact counterexamples. It establishes an open interval in a designed parameter family, rather than robustness to arbitrary preparation or decoder errors. An implementation perturbation can destroy exact recovery; no fault-tolerance claim follows from this interval.

## A rational-probability example

Choose

```math
x=\frac18,\qquad
u=i\sqrt7,\qquad
t=\frac{1+3u}{8}.
```

The coefficients simplify to

```math
\beta_2=-\frac{35+9u}{28},\qquad
\beta_1=-\frac34\beta_2
=\frac{105+27u}{112},\qquad
\gamma=\sqrt{\frac5{14}}.
\tag{9}
```

Their norms are

```math
|\beta_1|^2=\frac97,\qquad
|\beta_2|^2=\frac{16}{7},\qquad
\gamma^2=\frac5{14},\qquad
D=\frac{111}{14}.
```

Therefore

```math
\boxed{
p=\frac{224}{555}
=\frac25+\frac2{555},\qquad
Q=\frac{224}{111}
=2+\frac2{111}.
}
\tag{10}
```

The success advantage in this example is a rational number. The amplitudes themselves are algebraic, as specified in (9).

For the exact computational certificate, put $`v=\gamma`$ and work in

```math
\mathbb Q(u,v),\qquad
u^2=-7,\quad v^2=\frac5{14},\quad
\overline u=-u,\quad \overline v=v.
\tag{11}
```

Every field element is represented by four rational coefficients in the basis $`1,u,v,uv`$. The common decoder factor $`1/\sqrt2`$ and encoder factor $`1/\sqrt{5D}`$ are accounted for separately. This allows every encoder inner product, decoder row inner product, and effective logical Kraus matrix to be checked without floating-point arithmetic.

The resulting [committed certificate](../verification/expected/exact_certificate.json) has exactly eight nonzero scalar-identity effective Kraus operators for each pair and success $`224/555`$. It also checks the five disjoint-pair joint-success products and the sharp binary-profile score two.

## What is optimized

Equations (4)-(6) optimize the success furnished by the stated parameterized states and the stated recovery operators. They make no claim that another decoder for one of these encoders cannot do better.

For unrestricted finite-dimensional pentagon recovery, [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026) give the upper bound $`Q\le\sqrt5`$. The present attained value gives the rigorous interval

```math
\frac{16}{1+4\sqrt3}
\le Q_{\mathrm{best}}\le\sqrt5.
```

The strict inequality above two is sufficient for the access-profile separation and five-carrier minimality. Closing the remaining interval is a different question.
