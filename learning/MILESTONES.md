# Milestone map: nonclassical quantum access

This map identifies 30 conceptual milestones intrinsic to the project. The IDs describe parts of the scientific argument, independently of any reader's prior knowledge. Each dependency points to an earlier milestone; the source pointers lead to the definitions, statements, and proofs that give the milestone its precise content.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) supplies the verified reading map and the translation between book notation and project notation. Primary research sources remain necessary for the imported access-structure, recovery-profile, and graph theorems. The [repository overview](../README.md) gives the main result and the canonical science pages.

## Allocation and structure

| Phase | Milestones | Local-to-global progression | Integration point |
|---|---|---|---|
| I. Background and preliminaries | M01–M12 | Amplitudes and registers, then physical operations and exact recovery, then a complete operational probability model | M12 assembles the definitions and proof obligations of the five-pair task |
| II. Narrative and innovation | M13–M30 | Sparse amplitudes, then an isometric encoder and physical pair filter, then the full recovery profile, its comparison theorem, and its physical scope | M30 integrates construction, separation, minimality, evidence, and limitations |

The **12 + 18 allocation** reflects the argument's structure. Twelve preliminary milestones isolate the channel language needed to state exact conclusive recovery and its comparison class. Eighteen research milestones give separate attention to source normalization, the coherent flag, decoder validity, logical exactness, optimization, the unrestricted binary-code benchmark, and the externally supported minimality claim. These are distinct scientific obligations.

## Phase I: background and preliminaries

<a id="m01"></a>
### M01. Amplitudes, support, and orthogonality

**ID and phase:** M01 · Phase I, background and preliminaries.

**Central question:** Which linear-algebraic properties of sparse state vectors determine their norms, overlaps, and interference?

**Understanding target:** Complex amplitudes, computational-basis support, inner products, adjoints, and normalization. The distinction between adding amplitudes for the same basis word and adding probabilities for orthogonal words is essential to both the source-state norms and the later cancellation argument.

**Dependencies and story role:** None. This is the local mathematical foundation for every source coefficient and decoder row.

**Conceptual connection:** Disjoint support gives orthogonality; coincident support permits interference. The construction uses both properties for different purposes.

**Source pointers:** Watrous §§1.1.1, “Complex Euclidean spaces,” and 1.1.2, “Linear operators,” in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [bridge notation](WATROUS_BRIDGE.md#notation-and-normalization); [the two source states](../science/construction.md#the-two-source-states).

<a id="m02"></a>
### M02. Registers, tensor factors, and carrier blocks

**ID and phase:** M02 · Phase I, background and preliminaries.

**Central question:** What is a physical carrier, and how are its internal registers distinguished from independently erasable systems?

**Understanding target:** Tensor products, subsystem labels, ordered tensor factors, and regrouping registers without changing the physical partition. Each carrier in this project contains a ququart and a flag qubit, while erasure acts on the complete carrier.

**Dependencies and story role:** [M01](#m01). Establishes the tensor-factor accounting that fixes which operations are local to a surviving pair.

**Conceptual connection:** A Hilbert-space dimension and a carrier count describe different resources. Bundling several qubits into one carrier changes the erasure model.

**Source pointers:** Watrous §1.1.1, tensor products of vectors, in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), and §2.1.1, “Registers and classical state sets,” in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [the physical encoder](../science/construction.md#the-physical-encoder); [resource accounting](../science/interpretation.md#5-resource-accounting).

<a id="m03"></a>
### M03. Reduced states and the erased environment

**ID and phase:** M03 · Phase I, background and preliminaries.

**Central question:** What information remains accessible after some tensor factors are erased?

**Understanding target:** Density operators, partial trace, reduced states, and purification. Orthogonal erased records remove coherence between their corresponding surviving branches even when the global encoded state is pure.

**Dependencies and story role:** [M01](#m01), [M02](#m02). Converts physical erasure into a precise operation on a multipartite state.

**Conceptual connection:** Erasure is a change of accessible subsystem, not a measurement result that the decoder may freely retrieve. The erased flags later explain why the two flag branches contribute incoherently to the successful channel.

**Source pointers:** Watrous §§2.1.2, “Quantum states of registers,” and 2.1.3, “Reductions and purifications of quantum states,” in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [encoding and heralded recovery](../science/model.md#encoding-and-heralded-recovery); [why the flag is coherent](../science/construction.md#why-the-flag-is-coherent).

<a id="m04"></a>
### M04. Physical channels and successful subchannels

**ID and phase:** M04 · Phase I, background and preliminaries.

**Central question:** Which linear maps describe deterministic evolution, and which describe a selected successful outcome?

**Understanding target:** Complete positivity, trace preservation, and trace nonincrease, including their behavior on an input entangled with another system. An encoder is a channel; a successful decoder is a CP trace-nonincreasing map.

**Dependencies and story role:** [M01](#m01), [M03](#m03). Supplies the physical admissibility conditions for the two operations compared in the main channel identity.

**Conceptual connection:** Deterministic encoding and probabilistic recovery are compatible. The adjective “probabilistic” concerns the accepted recovery branch and does not make the encoder itself nonphysical or postselected.

**Source pointers:** Watrous §§2.2.1–2.2.2 and Theorems 2.22 and 2.26 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [exact conclusive recovery in the bridge](WATROUS_BRIDGE.md#exact-conclusive-recovery); [encoding and heralded recovery](../science/model.md#encoding-and-heralded-recovery).

<a id="m05"></a>
### M05. Kraus operators, effects, and complete instruments

**ID and phase:** M05 · Phase I, background and preliminaries.

**Central question:** How does a collection of successful Kraus operators become a physically complete success/failure procedure?

**Understanding target:** Kraus representations, the success effect $`\sum_a K_a^\dagger K_a`$, its upper bound by the identity, and completion by a failure outcome. Physical validity must hold on the full decoder input space, including states outside the code.

**Dependencies and story role:** [M04](#m04). Establishes the criterion used later to validate the sparse pair filter and its flagged extension.

**Conceptual connection:** A correct action on chosen codewords does not by itself establish a valid operation. The contraction condition is a separate requirement.

**Source pointers:** Watrous §2.2.2, Theorem 2.22, and §2.3.2, “Basic notions concerning measurements,” including instruments on printed pp. 111–113, in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [the bridge filtering example](WATROUS_BRIDGE.md#a-complete-filtering-example); [two successful Kraus operators](../science/recovery.md#two-successful-kraus-operators).

<a id="m06"></a>
### M06. Isometric encoding and dilation

**ID and phase:** M06 · Phase I, background and preliminaries.

**Central question:** When does a pair of proposed encoded vectors define a deterministic encoding of an arbitrary qubit?

**Understanding target:** The isometry condition $`V^\dagger V=I`$, orthonormal encoded columns, and the relationship between channel, Kraus, and Stinespring representations. Any environment in an implementation must have a stated physical location and accessibility.

**Dependencies and story role:** [M02](#m02), [M04](#m04), [M05](#m05). Sets the normalization standard that the source vectors must satisfy before they can represent an encoder.

**Conceptual connection:** A useful entangled source state and a trace-preserving encoding channel are different mathematical objects. Their relationship requires the correct reference marginal or, equivalently for a pure encoding, orthonormal columns.

**Source pointers:** Watrous §2.2.2 and Corollary 2.27 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [coherent flags and a valid encoder](WATROUS_BRIDGE.md#coherent-flags-and-a-valid-encoder); [the physical encoder](../science/construction.md#the-physical-encoder).

<a id="m07"></a>
### M07. Choi operators and reference preservation

**ID and phase:** M07 · Phase I, background and preliminaries.

**Central question:** How can a channel statement certify recovery of every unknown input and its external entanglement?

**Understanding target:** Vectorization, Choi representations, normalized versus unnormalized maximally entangled vectors, and equality of linear maps. Exact recovery must preserve off-diagonal logical operators as well as populations.

**Dependencies and story role:** [M01](#m01), [M04](#m04), [M05](#m05), [M06](#m06). Gives the representation-independent meaning of the project's exactness claim.

**Conceptual connection:** A Bell-reference calculation certifies a channel only when it uses the correct normalization and establishes the required operator equality. High numerical fidelity and exact equality have different evidentiary roles.

**Source pointers:** Watrous §1.1.2, vectorization on printed pp. 23–24, in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), and §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [bridge notation](WATROUS_BRIDGE.md#notation-and-normalization); [reference-state formulation](../science/construction.md#reference-state-formulation).

<a id="m08"></a>
### M08. Exact identity subchannels and environment independence

**ID and phase:** M08 · Phase I, background and preliminaries.

**Central question:** What structural condition makes a heralded successful map exactly proportional to the identity?

**Understanding target:** The rank-one Choi structure of the identity channel, scalar-identity effective Kraus operators, and the absence of logical information in the successful branch's environment. The proportionality constant fixes an input-independent success probability.

**Dependencies and story role:** [M03](#m03), [M05](#m05), [M06](#m06), [M07](#m07). Identifies the exact algebraic target for the recovery calculation.

**Conceptual connection:** Matching the correct basis outputs is insufficient unless the environment also matches. The same criterion later constrains arbitrary decoders in the unflagged comparison.

**Source pointers:** Watrous §2.2.2 and Theorem 2.22 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [reading the pentagon recovery proof](WATROUS_BRIDGE.md#reading-the-pentagon-recovery-proof); [exhaustive source-state calculation](../science/recovery.md#exhaustive-source-state-calculation).

<a id="m09"></a>
### M09. Disjoint operations and exact no-cloning

**ID and phase:** M09 · Phase I, background and preliminaries.

**Central question:** Why can two disjoint subsets not both succeed in exact universal recovery on the same encoded input?

**Understanding target:** Jointly applying completed instruments on disjoint factors, CP ordering of their marginal success maps, and the rank-one-Choi argument that reduces a nonzero joint-success branch to universal cloning.

**Dependencies and story role:** [M02](#m02), [M05](#m05), [M07](#m07), [M08](#m08). Provides the local-to-global exclusion principle behind the benchmark.

**Conceptual connection:** Heralded failure does not remove the no-cloning restriction for an arbitrary unknown input. Exactness makes every simultaneous success branch subject to the same universal constraint.

**Source pointers:** Watrous §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) for the CP/Choi machinery; [why disjoint exact recoveries are exclusive](../science/access_profiles.md#why-disjoint-exact-recoveries-are-exclusive); [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026) for the recovery-profile framework and constraints.

<a id="m10"></a>
### M10. Operational profiles, capabilities, and classical mixtures

**ID and phase:** M10 · Phase I, background and preliminaries.

**Central question:** Which probability vectors are being compared, and what randomness is allowed in the comparison?

**Understanding target:** Assigned recovery probabilities versus an encoder's optimized capabilities; binary success/abort profiles; input-independent lotteries over arbitrary quantum codes; and downward closure under deliberate aborts. A zero assigned probability is not a secrecy claim.

**Dependencies and story role:** [M04](#m04), [M05](#m05), [M08](#m08). Defines the comparison class before any special code or graph bound is invoked.

**Conceptual connection:** Convexity describes mixing complete protocols, while postselected filtering can have input-dependent branch weights. These two uses of probability must remain distinct.

**Source pointers:** Watrous §1.2.1, “Analysis and convexity,” in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [the arbitrary-code benchmark in the bridge](WATROUS_BRIDGE.md#the-arbitrary-code-benchmark); [operational probabilities and optimal capabilities](../science/access_profiles.md#operational-probabilities-and-optimal-capabilities); [the deterministic-mixture benchmark](../science/access_profiles.md#the-deterministic-mixture-benchmark).

<a id="m11"></a>
### M11. Query geometry and disjointness graphs

**ID and phase:** M11 · Phase I, background and preliminaries.

**Central question:** How does a collection of alternative surviving subsets become a graph of recovery constraints?

**Understanding target:** A graph vertex denotes a queried subset, and an edge denotes physical disjointness. Independent sets encode pairwise-intersecting success families; clique inequalities express the exclusivity of disjoint exact recoveries.

**Dependencies and story role:** [M02](#m02), [M09](#m09), [M10](#m10). Translates physical locality into the combinatorial language needed for the global comparison.

**Conceptual connection:** The cycle drawn on physical carriers and the disjointness graph drawn on queries are different constructions, even when both happen to be five-cycles. Query count alone does not establish carrier minimality.

**Source pointers:** [The arbitrary-code benchmark in the bridge](WATROUS_BRIDGE.md#the-arbitrary-code-benchmark); [binary profiles and the disjointness graph](../science/access_profiles.md#binary-profiles-and-the-disjointness-graph); [the pentagon bound](../science/access_profiles.md#the-pentagon-bound-is-exactly-two); [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026) for the research-specific graph framework.

<a id="m12"></a>
### M12. Integration: the complete five-pair recovery problem

**ID and phase:** M12 · Phase I, background and preliminaries.

**Central question:** What complete set of mathematical and physical obligations defines the claim this project must establish?

**Understanding target:** One encoder chosen before erasure; five alternative pair decoders; exact channel identities with reference preservation; valid success/failure instruments; an input-independent binary-code benchmark; and explicit carrier and assistance assumptions.

**Dependencies and story role:** [M01](#m01)–[M11](#m11). Integrates Phase I from local amplitudes and operations into the global operational problem.

**Conceptual connection:** Constructing a valid code, proving exact recovery, and proving a separation from a specified comparison class are separate obligations whose conjunction gives the research statement.

**Source pointers:** [Verified Watrous reading map](WATROUS_BRIDGE.md#verified-reading-map); [the operational model](../science/model.md#encoding-and-heralded-recovery); [the five-pair task](../science/model.md#the-five-pair-erasure-task); [the main theorem](../science/model.md#main-theorem); [the repository overview](../README.md).

## Phase II: narrative and innovation

<a id="m13"></a>
### M13. The local coefficient family

**ID and phase:** M13 · Phase II, narrative and innovation.

**Central question:** How does one real parameter specify amplitudes that remain physically admissible?

**Understanding target:** The roles of $`x,t,\beta_1,\beta_2,\gamma`$, the allowed parameter domain, and the normalization constraints shared by the source and decoder. The square root defining $`\gamma`$ must remain real throughout the claimed family.

**Dependencies and story role:** [M01](#m01), [M05](#m05), [M12](#m12). Starts the construction at its local scalar data before assembling global states.

**Conceptual connection:** Decoder admissibility and amplitude matching are linked through the same coefficients. A useful algebraic ansatz becomes a physical family only after these constraints are checked.

**Source pointers:** Watrous §1.1.2 in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [one parameter](../science/construction.md#one-parameter); [two successful Kraus operators](../science/recovery.md#two-successful-kraus-operators).

<a id="m14"></a>
### M14. Sparse source states and cyclic symmetry

**ID and phase:** M14 · Phase II, narrative and innovation.

**Central question:** How do the local coefficients assemble into two orthogonal, cyclically invariant five-site source states?

**Understanding target:** The defect and background supports of $`f`$ and $`g`$, their distinct basis-word orbits, their norms, and exact invariance under cyclic translation. The source norms are unequal throughout the strict-advantage interval.

**Dependencies and story role:** [M01](#m01), [M02](#m02), [M13](#m13). Builds the first global objects from the local amplitude data.

**Conceptual connection:** Support separates the two logical components, while symmetry later transports one local recovery proof to all five ordered pairs.

**Source pointers:** Watrous §§1.1.1–1.1.2 in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [the two source states](../science/construction.md#the-two-source-states); [the amplitude mechanism](../science/interpretation.md#1-the-filter-matches-amplitudes-and-cancels-false-outcomes).

<a id="m15"></a>
### M15. The biased-source normalization obstruction

**ID and phase:** M15 · Phase II, narrative and innovation.

**Central question:** At the advantageous parameters, why does the convenient reference-source vector not yet define a valid encoder of an arbitrary qubit?

**Understanding target:** When $`D\ne8`$, the unequal source norms produce a nonmaximally mixed reference marginal, so normalizing the total source state is insufficient to make its associated map trace preserving. At $`x=0`$ and $`x=1/4`$, one has $`D=8`$ and this normalization obstruction is absent.

**Dependencies and story role:** [M06](#m06), [M07](#m07), [M14](#m14). Identifies the normalization obstacle that the flag construction resolves.

**Conceptual connection:** A source can exhibit useful conclusive entanglement extraction while failing the input-normalization requirement of a deterministic encoding channel. Converting the source into a code is a substantive step.

**Source pointers:** Watrous §2.2.2, Theorem 2.26 and Corollary 2.27, in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [reference-state formulation](../science/construction.md#reference-state-formulation); [the flag balances unequal source weights](../science/interpretation.md#2-the-flag-balances-unequal-source-weights).

<a id="m16"></a>
### M16. Coherent flags complete the encoder

**ID and phase:** M16 · Phase II, narrative and innovation.

**Central question:** How do the two flag branches preserve the favorable source amplitudes while forming a deterministic isometry?

**Understanding target:** The exchanged $`f,g`$ branches, the isometry condition, and the complete-instrument identity for the two branch maps. Away from $`D=8`$, their input-dependent occurrence weights distinguish these displayed branches from an input-independent lottery over encoding channels.

**Dependencies and story role:** [M05](#m05), [M06](#m06), [M10](#m10), [M15](#m15). Resolves the source normalization obstruction without discarding the amplitude relationships needed for recovery.

**Conceptual connection:** Coherent implementation makes the whole encoder pure, while the branch maps individually behave as filters. Every flag is stored in an erasable carrier.

**Source pointers:** Watrous §2.2.2 and §2.3.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [coherent flags and a valid encoder](WATROUS_BRIDGE.md#coherent-flags-and-a-valid-encoder); [the physical encoder](../science/construction.md#the-physical-encoder); [why the flag is coherent](../science/construction.md#why-the-flag-is-coherent).

<a id="m17"></a>
### M17. A valid two-site success filter

**ID and phase:** M17 · Phase II, narrative and innovation.

**Central question:** Why do the two sparse recovery matrices define a physical successful operation on every pair input?

**Understanding target:** The four stacked decoder rows, their orthonormality, the coisometry condition, and the resulting projector-valued success effect. This establishes complete positivity and trace nonincrease independently of how the filter acts on the code.

**Dependencies and story role:** [M05](#m05), [M13](#m13), [M16](#m16). Supplies a physically admissible local operation before proving its logical action.

**Conceptual connection:** Sparse supports simplify both normalization and interference calculations, but these serve different purposes. Projector-valued success effects later also support the compatible-measurement interpretation.

**Source pointers:** Watrous §2.2.2 and §2.3.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [the bridge filtering example](WATROUS_BRIDGE.md#a-complete-filtering-example); [two successful Kraus operators](../science/recovery.md#two-successful-kraus-operators).

<a id="m18"></a>
### M18. Cancellation and matched erased environments

**ID and phase:** M18 · Phase II, narrative and innovation.

**Central question:** Which amplitude identities remove every false logical output and preserve coherence in every accepted branch?

**Understanding target:** The exhaustive support analysis, cancellation for an outside defect, and equality of the erased-environment vectors arising from the two source components. Both absence of wrong outputs and equality of correct amplitudes are necessary.

**Dependencies and story role:** [M08](#m08), [M13](#m13), [M14](#m14), [M17](#m17). Establishes the central local recovery relation.

**Conceptual connection:** Destructive interference enforces rejection, while environment matching protects the unknown logical superposition. The proof depends on tracking erased words before tracing them out.

**Source pointers:** Watrous §2.1.3 and §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [reading the pentagon recovery proof](WATROUS_BRIDGE.md#reading-the-pentagon-recovery-proof); [three matching identities](../science/recovery.md#three-identities-that-match-the-logical-amplitudes); [exhaustive source-state calculation](../science/recovery.md#exhaustive-source-state-calculation).

<a id="m19"></a>
### M19. The exact physical pair channel

**ID and phase:** M19 · Phase II, narrative and innovation.

**Central question:** How do flag reading, conditional correction, and erased systems combine into one exact logical identity subchannel?

**Understanding target:** The full flagged Kraus operators, rejection of unequal surviving flags, orthogonal erased flag records, and the eight nonzero effective logical Kraus operators. Their scalar-identity form establishes the complete channel equality and its input-independent probability.

**Dependencies and story role:** [M07](#m07), [M08](#m08), [M16](#m16), [M17](#m17), [M18](#m18). Completes the local proof for one ordered pair, including physical validity outside the encoded subspace.

**Conceptual connection:** Input-dependent intermediate branch weights can combine into an input-independent successful channel. Reference preservation follows from the linear-map identity.

**Source pointers:** Watrous §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [exact conclusive recovery in the bridge](WATROUS_BRIDGE.md#exact-conclusive-recovery); [recovery with the physical flags](../science/recovery.md#recovery-with-the-physical-flags).

<a id="m20"></a>
### M20. What separate normalization loses

**ID and phase:** M20 · Phase II, narrative and innovation.

**Central question:** What comparison isolates the role of the flag for these particular source states?

**Understanding target:** Within the strict-advantage interval, the separately normalized unflagged encoder, the exact upper bound on its pair-recovery probability over arbitrary successful decoders, and an attaining filter. The bound follows from the defect's location and rank-one-Choi rigidity, rather than a restricted numerical search.

**Dependencies and story role:** [M07](#m07), [M14](#m14), [M17](#m17), [M18](#m18), [M19](#m19). Explains the mechanism by comparing two encoders built from the same source words.

**Conceptual connection:** Normalization can change the operational recovery problem even when the underlying supports are unchanged. The component lemma concerns these source states and does not assert that every advantageous code must use flags.

**Source pointers:** Watrous §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [the component lemma](../science/interpretation.md#component-lemma); [the equivalent GHZ-phase form](../science/interpretation.md#4-equivalent-ghz-phase-form).

<a id="m21"></a>
### M21. One encoder and all five pair recoveries

**ID and phase:** M21 · Phase II, narrative and innovation.

**Central question:** Why does the single-pair proof establish one common encoding with the advertised recovery probability on every cycle edge?

**Understanding target:** The role of cyclic invariance, ordered pairs including $`(4,0)`$, relabeling of erased systems, and the shared decoder matrices. The five probabilities belong to alternative operations on one common code.

**Dependencies and story role:** [M02](#m02), [M14](#m14), [M16](#m16), [M19](#m19). Integrates the local construction and channel proof into a complete five-query recovery profile.

**Conceptual connection:** Symmetry transports a proved channel identity; it does not authorize simultaneous recovery from overlapping queries. The score sums alternative success probabilities.

**Source pointers:** [Reading the pentagon recovery proof](WATROUS_BRIDGE.md#reading-the-pentagon-recovery-proof); [all five pairs](../science/recovery.md#all-five-pairs); [the five-pair task](../science/model.md#the-five-pair-erasure-task); [the main theorem](../science/model.md#main-theorem).

<a id="m22"></a>
### M22. The attainable family and its analytic optimum

**ID and phase:** M22 · Phase II, narrative and innovation.

**Central question:** Which parameter maximizes the displayed success probability, and what does that optimization actually establish?

**Understanding target:** The scalar normalization function, the closed-form optimum within the allowed parameter interval, and the full strict-advantage interval. The optimization concerns the specified encoder-decoder family and does not range over all decoders or all encoders.

**Dependencies and story role:** [M13](#m13), [M19](#m19), [M21](#m21). Converts the exact channel construction into an attained quantitative lower bound.

**Conceptual connection:** A family extremum and a global operational optimum have different quantifiers. An open interval of exact designed constructions also differs from robustness under arbitrary implementation errors.

**Source pointers:** [A one-variable normalization](../science/parameter_family.md#a-one-variable-normalization); [exact family optimum](../science/parameter_family.md#exact-family-optimum); [the entire strict-advantage interval](../science/parameter_family.md#the-entire-strict-advantage-interval); [what is optimized](../science/parameter_family.md#what-is-optimized); [bridge claim boundaries](WATROUS_BRIDGE.md#resources-and-claim-boundaries).

<a id="m23"></a>
### M23. Exact certificates and the scope of numerical evidence

**ID and phase:** M23 · Phase II, narrative and innovation.

**Central question:** Which claims are established by the rational certificate, the family algebra, and the numerical reconstruction?

**Understanding target:** The algebraic number field of the rational member, exact contraction of every effective Kraus operator, and the distinct role of floating-point diagnostics. The written proof connects scalar identities to a physical exact-recovery theorem.

**Dependencies and story role:** [M07](#m07), [M17](#m17), [M19](#m19), [M21](#m21), [M22](#m22). Connects the analytic result to independently reconstructible finite evidence without enlarging that evidence's scope.

**Conceptual connection:** Exact arithmetic certifies finite identities; analytic arguments establish the entire parameter family; external theorem statements require their own cited proofs. A numerical residual is neither a universal proof nor an exactness certificate.

**Source pointers:** [The rational-probability example](../science/parameter_family.md#a-rational-probability-example); [exact certificate](../verification/README.md#exact-certificate-for-the-rational-member); [exact family algebra](../verification/README.md#exact-algebra-for-the-parameter-family); [verification proof boundaries](../verification/README.md#proof-boundaries); [the committed certificate](../verification/expected/exact_certificate.json).

<a id="m24"></a>
### M24. The unrestricted binary-code benchmark

**ID and phase:** M24 · Phase II, narrative and innovation.

**Central question:** Why is the pentagon comparison valid against every binary quantum-access protocol, regardless of code structure or finite carrier dimension?

**Understanding target:** No-cloning necessity, the realization of intersecting access families using the general QSS theorem, the stable-set description of the binary-mixture body, and the sharp pentagon bound. Routing supplies attainability, while the upper bound includes arbitrary entangled codes and deliberate aborts.

**Dependencies and story role:** [M09](#m09), [M10](#m10), [M11](#m11), [M12](#m12). Establishes the comparison theorem independently of the special construction's resources.

**Conceptual connection:** QSS realization is used to characterize feasible deterministic patterns. Secrecy on every failed or unqueried subset is not imposed on the project's general protocols.

**Source pointers:** [The arbitrary-code benchmark in the bridge](WATROUS_BRIDGE.md#the-arbitrary-code-benchmark); [binary profiles and the disjointness graph](../science/access_profiles.md#binary-profiles-and-the-disjointness-graph); [the sharp pentagon bound](../science/access_profiles.md#the-pentagon-bound-is-exactly-two); [Gottesman's general-access theorem](../references/RELATED_WORK.md#gottesman2000).

<a id="m25"></a>
### M25. The nonclassical-profile separation

**ID and phase:** M25 · Phase II, narrative and innovation.

**Central question:** What exactly is separated by the attained score, and which optimization question remains open?

**Understanding target:** Comparison of the common code's five exact probabilities with the binary-mixture inequality; extension of this separation to any full operational profile containing those coordinates; and the distinction between the attained score and the universal Lovász upper bound.

**Dependencies and story role:** [M21](#m21), [M22](#m22), [M24](#m24). Joins the constructive and impossibility arguments into the project's principal separation.

**Conceptual connection:** The displayed decoders need not be optimal for their encoder to establish a strict separation. Larger optimal probabilities would preserve the violation, while still leaving unrestricted Lovász saturation unresolved.

**Source pointers:** [The main theorem](../science/model.md#main-theorem); [the pentagon comparison](../science/access_profiles.md#the-pentagon-bound-is-exactly-two); [what is optimized](../science/parameter_family.md#what-is-optimized); [Alhejji et al.'s direct precedent and bound](../references/RELATED_WORK.md#alhejji2026).

<a id="m26"></a>
### M26. Why five carriers are minimal

**ID and phase:** M26 · Phase II, narrative and innovation.

**Central question:** Which external result excludes this separation for every query family on four or fewer carriers?

**Understanding target:** The constructive small-carrier classification, its binary realizations, and preservation of the binary-mixture body under permutations, mixing, unused carriers, and coordinatewise aborts. Minimality holds with finite but unrestricted carrier dimensions.

**Dependencies and story role:** [M10](#m10), [M24](#m24), [M25](#m25). Combines an imported necessity result with the new five-carrier sufficiency result.

**Conceptual connection:** A smallest imperfect query graph does not by itself establish a smallest carrier count. The classification concerns the full operational body and supplies the required stronger statement.

**Source pointers:** [Why five carriers are minimal in the bridge](WATROUS_BRIDGE.md#why-five-carriers-are-minimal); [five-carrier minimality](../science/access_profiles.md#five-carrier-minimality); [Alhejji et al.](../references/RELATED_WORK.md#alhejji2026); [threshold QSS constructions](../references/RELATED_WORK.md#cleve1999).

<a id="m27"></a>
### M27. Correlated erasures and antidegradability

**ID and phase:** M27 · Phase II, narrative and innovation.

**Central question:** How can the code improve exact conclusive transmission for the specified erasure law while the physical channel has zero unassisted quantum capacity?

**Understanding target:** The uniformly selected adjacent-pair channel, the distinction between correlated survival and independent erasures, and the explicit environmental simulation of the receiver's output. One-shot heralded transmission and asymptotic unassisted capacity are different operational quantities.

**Dependencies and story role:** [M03](#m03), [M06](#m06), [M08](#m08), [M21](#m21), [M25](#m25). Places the profile separation inside a concrete communication channel without inferring a capacity advantage.

**Conceptual connection:** Matching individual carrier survival probabilities does not identify a joint erasure distribution. The anti-degrading map explains why the construction is compatible with a zero-capacity channel.

**Source pointers:** Watrous §2.2.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) for channel and dilation representations; [the correlated-erasure channel](../science/interpretation.md#6-the-correlated-erasure-channel); [Ahmed and Smith](../references/RELATED_WORK.md#ahmed2026); [Cubitt, Ruskai, and Smith](../references/RELATED_WORK.md#cubitt2008).

<a id="m28"></a>
### M28. Graph structure and the secondary contextuality interpretation

**ID and phase:** M28 · Phase II, narrative and innovation.

**Central question:** What additional interpretation follows from the actual success projectors, and which assumptions does it require?

**Understanding target:** Perfect-graph background, commuting tests on disjoint pairs, zero joint-success probability on the code, and the compatible-context statistics of the rational member. The contextuality statement concerns the absence of a common global outcome distribution under the specified ideal compatibility assumptions.

**Dependencies and story role:** [M05](#m05), [M09](#m09), [M11](#m11), [M17](#m17), [M19](#m19), [M23](#m23), [M24](#m24). Relates the operational result to established graph and measurement theory after the physical tests have been defined.

**Conceptual connection:** The protocol comparison is established without a hidden-variable model. The compatible-measurement corollary uses the same projectors but does not constitute Bell nonlocality or device-independent certification.

**Source pointers:** Watrous §2.3.2 in [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [perfect query graphs](../science/access_profiles.md#perfect-query-graphs-standard-structural-context); [the precise contextuality statement](../science/access_profiles.md#secondary-interpretation-as-compatible-measurement-contextuality); [Chvátal](../references/RELATED_WORK.md#chvatal1975); [Cabello, Severini, and Winter](../references/RELATED_WORK.md#cabello2014).

<a id="m29"></a>
### M29. Resources and physical boundaries

**ID and phase:** M29 · Phase II, narrative and innovation.

**Central question:** Which resources and guarantees belong to the demonstrated construction, and which would define a different problem?

**Understanding target:** Five erasable blocks, uniform local dimension eight, the optional reduced flag placement, joint access to a surviving pair, and the absence of retained sender assistance. The claims do not optimize local dimension, establish an LOCC decoder, impose general QSS secrecy, or provide robustness under arbitrary implementation noise.

**Dependencies and story role:** [M02](#m02), [M10](#m10), [M16](#m16), [M21](#m21), [M22](#m22), [M26](#m26), [M27](#m27). Collects the physical assumptions needed to interpret the full theorem correctly.

**Conceptual connection:** Carrier minimality, local-dimension cost, and fault-tolerance performance are independent questions. Exact algebraic recovery under a specified erasure model answers only the claims proved for that model.

**Source pointers:** [Resources and claim boundaries in the bridge](WATROUS_BRIDGE.md#resources-and-claim-boundaries); [resource accounting](../science/interpretation.md#5-resource-accounting); [scope of the separation](../science/interpretation.md#7-scope-of-the-separation); [the strict-advantage interval and its scope](../science/parameter_family.md#the-entire-strict-advantage-interval); [model assumptions](../science/model.md#encoding-and-heralded-recovery).

<a id="m30"></a>
### M30. Integration: the complete scientific claim

**ID and phase:** M30 · Phase II, narrative and innovation.

**Central question:** How do the construction, exact proof, unrestricted comparison, external classification, and resource limits combine into one defensible research statement?

**Understanding target:** The full implication chain from physical encoder and decoder to an exact nonclassical recovery profile and five-carrier minimality. The provenance of every step distinguishes the new construction and component comparison from imported QSS, graph, channel, and small-carrier theorems.

**Dependencies and story role:** [M12](#m12), [M20](#m20), [M23](#m23), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). Integrates Phase II from local amplitudes to the global result, its evidence, and its remaining open bounds.

**Conceptual connection:** A strict attainable separation can be complete as a theorem while the unrestricted optimum, minimal local dimension, and noisy implementation questions remain unresolved.

**Source pointers:** [The main theorem](../science/model.md#main-theorem); [the exact recovery proof](../science/recovery.md); [the benchmark and minimality](../science/access_profiles.md); [related work and attribution](../references/RELATED_WORK.md); [verification proof boundaries](../verification/README.md#proof-boundaries); [the Watrous bridge](WATROUS_BRIDGE.md); [the repository overview](../README.md).
