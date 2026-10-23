# Verification

The scientific proof and the computational checks have distinct roles. [Recovery](../science/recovery.md) proves the exact channel identity for the entire stated family. [Parameter family](../science/parameter_family.md) gives its elementary optimum. The scripts reconstruct finite identities from the published formulas; they do not load numerical optimizer output.

Use Python 3.11 or later. The exact commands require only the standard library. NumPy is needed only for the optional numerical reconstruction.

## Exact certificate for the rational member

From the repository root:

```sh
python -S verification/verify_exact.py --check verification/expected/exact_certificate.json
```

Expected result: JSON with `"status": "PASS"`, five pair-channel entries each reporting `"success_probability": "224/555"`, and `"success_sum": "224/111"`. The complete expected output is committed as [exact_certificate.json](expected/exact_certificate.json).

The script constructs the $`x=1/8`$ encoder and decoder in

```math
\mathbb Q(u,v),\qquad
u^2=-7,\quad v^2=\frac5{14},\quad
\overline u=-u,\quad \overline v=v.
```

Every scalar has four rational coefficients in the basis $`1,u,v,uv`$. The common encoder and decoder normalization factors are tracked separately. All comparisons in this certificate are exact; no floating-point value or tolerance enters them.

### What is checked

| Check | Mathematical implication |
|---|---|
| Source coefficients, support, norms, and cyclic invariance | The sparse states agree with the published construction |
| The two full flagged encoder columns have the required Gram matrix | $`V^\dagger V=I_2`$ |
| The four rows of $`L=\sqrt2K`$ have Gram matrix $`2I_4`$ | The successful ququart operation is contractive; its equal-flag extension is contractive on the full physical pair |
| All erased-carrier basis labels, including flags, are retained during contraction | Distinct environments are not combined coherently by mistake |
| Every effective logical Kraus matrix is a scalar identity | Exact recovery of arbitrary logical operators and reference entanglement |
| Eight nonzero effective Kraus matrices per pair | Their squared coefficients give exactly $`224/555`$ |
| Five disjoint-pair success-projector products vanish on both source words | Their flagged extensions have zero joint success on the entire code |
| Enumeration of all binary independent sets of the query graph | Eleven binary profiles, with maximum score two |

The contraction uses the ordered wraparound pair $`(4,0)`$ consistently. Unequal surviving flag values are rejected. The field implementation, physical contractions, and verification assertions are all contained in [verify_exact.py](verify_exact.py).

The script refuses to run under Python's `-O` or `-OO` modes, which disable assertions. A failed identity or a mismatch with the committed certificate exits unsuccessfully.

To write the report to a separate file:

```sh
python -S verification/verify_exact.py --output /tmp/nonclassical_access_exact.json
```

The committed output is an expected result, not an input to the scientific calculation. The `--check` option compares it with a freshly reconstructed report.

## Exact algebra for the parameter family

```sh
python -S verification/verify_family.py
```

Expected result: top-level `"status": "PASS"`, exact parameter-identity checks, and `"floating_channel_diagnostics": {"enabled": false}`. The report identifies the arithmetic and the scope of the checked algebra.

This mode checks the parameter formulas, normalization, strict-advantage condition, rational example, and the square-completion identity

```math
D-(1+4\sqrt3)=\frac{(2(1-x)-\sqrt3)^2}{1-x}.
```

The amplitude-matching identities and the proof of exact recovery are established by the exhaustive source-state calculation in [Recovery](../science/recovery.md). The inequality and parameter-domain arguments are in [Parameter family](../science/parameter_family.md). The script does not replace those analytic steps or claim an unrestricted-code optimum.

## Optional numerical reconstruction

Install the pinned dependency and run:

```sh
python -m pip install -r verification/requirements.txt
python verification/verify_family.py --numerical
```

The dependency is NumPy 2.3.5. This mode builds the full $`8^5\times2`$ encoding matrix and the physical pair Kraus operators independently of the exact verifier. For each pair it contracts the full effective channel, checks scalar-identity Kraus form, compares the normalized Choi operator with the predicted identity-channel Choi operator, and checks input-independent success and physical contraction.

The default numerical suite covers six parameter choices and thirty complete pair channels:

| Case | Parameter |
|---|---|
| Family optimum | $`x=1-\sqrt3/2`$ |
| Rational member | $`x=1/8`$ |
| Lower domain boundary | $`x=0`$ |
| Advantage boundary | $`x=1/4`$ |
| Upper domain boundary | $`x=3/4`$ |
| Conjugate optimum | Optimal $`x`$, with the opposite sign of the phase's imaginary part |

The JSON identifies the Python and NumPy versions, per-case probabilities, norms used for residuals, and the absolute tolerance. Floating residuals are diagnostics, not certificates of exact equality.

For selected cases or another member:

```sh
python verification/verify_family.py --numerical --case optimal
python verification/verify_family.py --numerical --case rational
python verification/verify_family.py --numerical --x 0.1 --orientation -1
```

The custom parameter must obey $`0\le x\le3/4`$. The optional setting `OPENBLAS_NUM_THREADS=1` can reduce overhead on systems using OpenBLAS; it is not needed for correctness.

## Proof boundaries

The exact certificate establishes one finite physical construction. The exact family algebra and the written proof establish the continuous family and its stated optimum. The arbitrary-dimension deterministic-mixture bound and five-carrier minimality additionally use the arguments and attributed results in [Access profiles](../science/access_profiles.md).

Neither script proves global optimality, minimum local dimension, noisy implementation robustness, or the correctness of a cited external theorem. Those are separate claims and are not inferred from a `PASS` report.
