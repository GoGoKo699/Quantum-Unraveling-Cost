# Thirty milestones through Quantum Unraveling Cost

[Repository](../README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [Scientific account](../science/README.md)

The route has two phases: twelve milestones develop the background from individual quantum systems to complete resource comparisons; eighteen reconstruct the project's argument from one weak slot to its global cost and robustness limits. The identifiers M01–M30 are fixed and follow one order.

The educational anchor is Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge University Press, 2017). Section numbers below follow the [publisher's verified second-edition contents](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf). These pointers identify the supporting tools; the linked project sources supply the particular monitored-process, smooth-rank, and Poisson results. The project uses root fidelity $`F`$, purified distance $`P=\sqrt{1-F^2}`$, and half trace distance $`D=\tfrac12\|\rho-\sigma\|_1`$; the [Wilde bridge](WILDE_BRIDGE.md#first-translate-the-error-convention) records the squared-fidelity and trace-norm translations for the versioned author companion.

## Phase I — Background and preliminaries

### M01

**Local quantum data and a reported sign**

- **Central question:** What information leaves one monitoring slot as quantum data, and what leaves as a classical report?
- **Target:** Identify the data qubits, their density operator, the sign register, and the local reference systems in the task.
- **Dependencies and story role:** Entry point. It supplies the objects used in every later milestone.
- **Conceptual connection:** A detector's classical outcome and the quantum system it disturbs are distinct outputs of one physical operation.
- **Project source:** [Model: accessible ports and causal simulation](../science/model.md#accessible-ports-and-causal-simulation).
- **Wilde pointer:** §§3.2, 4.1 and 4.2.

### M02

**Composite systems and the Schmidt spectrum**

- **Central question:** How is the entanglement of a pure state shared between the two laboratories represented?
- **Target:** Write the meter's Schmidt decomposition and distinguish its amplitudes, squared Schmidt probabilities, and Schmidt rank.
- **Dependencies and story role:** Uses M01. It introduces the spectrum that later prices the complete experiment.
- **Conceptual connection:** A two-qubit meter is local in time but bipartite in space; its tensor powers retain both structures.
- **Project source:** [Resource equivalence: one slot](../science/resource_equivalence.md#one-slot), especially the definition of $`|\phi_p\rangle`$.
- **Wilde pointer:** §§3.5, 3.6 and 3.8.

### M03

**Outcome probabilities and conditional backaction**

- **Central question:** Which part of a measurement description fixes its probabilities, and which part fixes its retained quantum output?
- **Target:** Relate a Kraus branch to its POVM effect and conditional output, retaining the branch's normalization.
- **Dependencies and story role:** Uses M01–M02. It prevents a simulator from satisfying only the sign statistics.
- **Conceptual connection:** The instrument contains the disturbance that can create entanglement, even when its effects look like a weak classical test.
- **Project source:** [Resource equivalence: one slot](../science/resource_equivalence.md#one-slot).
- **Wilde pointer:** §§4.2 and 4.6.

### M04

**Forgetting a record gives a quantum channel**

- **Central question:** What operation remains when the classical sign is ignored?
- **Target:** Sum the completely positive branches, identify the resulting channel, and preserve its action on a reference-entangled input.
- **Dependencies and story role:** Uses M03. It establishes the unread evolution that all later unravelings share.
- **Conceptual connection:** Discarding an output register is a physical map and can erase the distinction between different recorded experiments.
- **Project source:** [Model: fixed-time family](../science/model.md#fixed-time-family).
- **Wilde pointer:** §§4.4, 4.5 and 4.7.

### M05

**Environment access and recorded instruments**

- **Central question:** Why can changing the environment's readout produce different records without changing the unread channel?
- **Target:** Connect channel dilation, environmental measurement, and the induced classical–quantum instrument.
- **Dependencies and story role:** Uses M03–M04. It frames the project's question about the resource cost of an unraveling.
- **Conceptual connection:** The unread generator specifies less of the task than the environment record and its associated backaction.
- **Project source:** [Unraveling gap: exact unread evolution and recorded jumps](../science/unraveling_gap.md#exact-unread-evolution).
- **Wilde pointer:** §§5.1, 5.2 and 5.3.

### M06

**Shared entanglement as a charged resource**

- **Central question:** What can Alice and Bob do for free, and which initial shared resource is being counted?
- **Target:** State the LOCC model, deterministic initial Bell-pair budget, allowed local memories, and treatment of catalysts and returned systems.
- **Dependencies and story role:** Uses M02 and M04–M05. It fixes the operational meaning of every cost claim.
- **Conceptual connection:** Resource conversion has meaning only after the free operations and initial supply are specified.
- **Project source:** [Model: initially supplied entanglement](../science/model.md#initially-supplied-entanglement).
- **Wilde pointer:** §§6.1, 6.2 and 19.2.

### M07

**Schmidt rank and entanglement entropy**

- **Central question:** Why can a weak meter have low entropy while still requiring nonzero exact Schmidt rank?
- **Target:** Compare the meter's rank, entropy of either share, and their behavior under tensor products.
- **Dependencies and story role:** Uses M02 and M06. It separates the exact supply questions before asymptotics are introduced.
- **Conceptual connection:** Rank tracks which coherent terms must exist; entropy weights their probabilities.
- **Project source:** [Exact resources: exact Bell supply and pure-resource entropy](../science/exact_resources.md#exact-bell-pair-supply).
- **Wilde pointer:** §§3.8 and 11.1; §19.3 for the resource-conversion task.

### M08

**Preparing a pure shared resource**

- **Central question:** When can a finite maximally entangled supply prepare a chosen pure resource by LOCC?
- **Target:** Understand the project’s use of deterministic pure-state conversion and why a rank-$`R`$ truncated state fits a sufficiently large Bell supply.
- **Dependencies and story role:** Uses M06–M07. It supplies the preparation step of the matching upper bound.
- **Conceptual connection:** Entanglement dilution motivates preparing a cheaper resource before running the measurement circuit.
- **Project source:** [Bell cost: achievability](../science/bell_cost.md#achievability); the exact conversion criterion is credited in [related work](../references/RELATED_WORK.md#entanglement-cost-and-sequential-simulation).
- **Wilde pointer:** §§19.3–19.4 for entanglement manipulation; the project gives the required finite-rank application.

### M09

**Fidelity and a global approximation target**

- **Central question:** How is closeness to a pure resource quantified without an error growing with its ambient dimension?
- **Target:** Translate squared fidelity to the project's root-fidelity convention and relate pure-state overlap to purified distance.
- **Dependencies and story role:** Uses M02 and M08. It makes the retained Schmidt probability into an exact error criterion.
- **Conceptual connection:** A probability tail can control an entire normalized quantum state through fidelity.
- **Project source:** [Bell cost: resource and error being optimized](../science/bell_cost.md#resource-and-error-being-optimized).
- **Wilde pointer:** §§9.2–9.3. Keep the project's $`F`$ and $`P`$ definitions explicit during convention translation.

### M10

**Trace distance, effects, and contractivity**

- **Central question:** What does a bound on half trace distance guarantee for an unconditional measurement event?
- **Target:** Bound an effect's probability change, use contractivity under a physical map, and translate the factor of two in trace-norm conventions.
- **Dependencies and story role:** Uses M03–M04 and M09. It provides the error accounting needed for noisy-record robustness.
- **Conceptual connection:** Testing a complete output gives a controlled probability statement without conditioning on a rare event.
- **Project source:** [Bell cost: trace-distance error](../science/bell_cost.md#a-trace-distance-process-error); [noisy record: transferring the sector witness](../science/inefficient_record.md#transferring-the-sector-witness-through-a-process-error).
- **Wilde pointer:** §§9.1–9.3.

### M11

**Entanglement monotones with classical flags**

- **Central question:** How can an LOCC outcome branch support a resource lower bound while retaining its probability and failure outcomes?
- **Target:** Use relative entropy of entanglement and its selective LOCC monotonicity, including a public success flag.
- **Dependencies and story role:** Uses M06 and M10. It extends the available converse tools to mixed meter outputs.
- **Conceptual connection:** Postselection contributes its probability to an unconditional resource account.
- **Project source:** [Noisy record: entanglement required by the successful state](../science/inefficient_record.md#entanglement-required-by-the-successful-state).
- **Wilde pointer:** §11.8 and §19.2.

### M12

**Probability shells and changing sources**

- **Central question:** Which part of a many-copy compression argument depends on keeping the source distribution fixed?
- **Target:** Relate tensor-product Schmidt probabilities to classical strings, type multiplicities, and retained probability mass; identify that this project's $`p_N`$ changes with $`N`$.
- **Dependencies and story role:** Uses M07–M10. It completes the background needed for a fixed-time rare-event limit.
- **Conceptual connection:** Typical-subspace thinking motivates compression, while the actual changing-source tail must be calculated separately.
- **Project source:** [Bell cost: probability shells](../science/bell_cost.md#evaluating-the-rank-without-enumerating-bit-strings); [Poisson limit: fixed-time family](../science/poisson_limit.md).
- **Wilde pointer:** §§10.1, 14.2 and 15.1; §19.4 for the fixed-source asymptotic context.

## Phase II — Narrative and innovation

### M13

**Build the efficient weak parity slot**

- **Central question:** Which two-branch instrument measures $`Q=Z_A\otimes Z_B`$ weakly while retaining its efficient conditional output?
- **Target:** Reconstruct $`M_s`$, its positivity, its effect, and the relation between $`p`$ and measurement strength $`\eta`$.
- **Dependencies and story role:** Uses M01–M04 and M07. It fixes the one-slot object that the remainder of the argument prices.
- **Conceptual connection:** An operator identity joins the POVM and the coherent backaction.
- **Project source:** [Resource equivalence: one slot](../science/resource_equivalence.md#one-slot).
- **Wilde pointer:** §§4.2, 4.4 and 4.6.

### M14

**Match the slot to an exact unread semigroup**

- **Central question:** How does a fixed duration determine the weak-slot parameter as the number of accessible slots grows?
- **Target:** Recover $`p_N`$ from the parity-dephasing semigroup and distinguish its $`N^{-1}`$ scale from the signal's $`N^{-1/2}`$ scale.
- **Dependencies and story role:** Uses M04, M12 and M13. It fixes the asymptotic family before any resource expansion is taken.
- **Conceptual connection:** Exact finite-slot dynamics supplies a controlled bridge to weak continuous monitoring.
- **Project source:** [Unraveling gap: exact unread evolution](../science/unraveling_gap.md#exact-unread-evolution); [continuum: binary slots](../science/continuum_and_cadence.md#binary-slots-and-the-diffusive-equation).
- **Wilde pointer:** §§4.4 and 4.7; the semigroup and limiting calculation are developed in the project.

### M15

**Find the free comparison interfaces**

- **Central question:** Which recorded and unrecorded versions of this same noise admit an exact LOCC implementation?
- **Target:** Compare shared random local Pauli kicks, their public jump record, and the efficient weak sign record on reference-entangled inputs.
- **Dependencies and story role:** Uses M05–M06 and M13–M14. It establishes the physically meaningful comparison behind the cost separation.
- **Conceptual connection:** A generator does not determine the implementation resources of every record associated with it.
- **Project source:** [Unraveling gap: unread and recorded jump implementations](../science/unraveling_gap.md#the-recorded-jump-unraveling-is-also-free).
- **Wilde pointer:** §§4.5, 5.3 and 6.1.

### M16

**Implement one slot from a shared weak meter**

- **Central question:** How do local controlled operations and meter readout reproduce the complete nonlocal instrument?
- **Target:** Calculate the raw two-sign Kraus map and verify that grouping by the product sign preserves the required backaction.
- **Dependencies and story role:** Uses M03, M06, M08 and M13. It constructs the exact one-slot upper bound.
- **Conceptual connection:** A known entangled resource converts local interactions into a nonlocal measurement.
- **Project source:** [Resource equivalence: one slot](../science/resource_equivalence.md#one-slot); [primitive attribution](../references/RELATED_WORK.md#efficient-nonlocal-weak-measurements).
- **Wilde pointer:** §§4.6, 6.1 and 6.2.

### M17

**Recover the meter from fresh measured data**

- **Central question:** What entangled state can a local tester recover from every retained weak-measurement output?
- **Target:** Use fresh product inputs, the public sign, and local corrections to recover one fixed pure meter per slot.
- **Dependencies and story role:** Uses M02, M06, M13 and M16. It supplies the reverse resource conversion.
- **Conceptual connection:** The entanglement created by a requested operation constrains the resources of its simulator.
- **Project source:** [Resource equivalence: recovering the resource](../science/resource_equivalence.md#recovering-the-resource-from-the-process).
- **Wilde pointer:** §§3.8 and 19.2–19.3.

### M18

**Expose the full causal interface**

- **Central question:** What additional requirement appears when users can remove and archive the quantum output before the next slot?
- **Target:** Specify a causal tester with fresh probes and retained outputs, and formulate the whole-experiment error against arbitrary allowed interventions.
- **Dependencies and story role:** Uses M01, M06, M09–M10 and M17. It lifts the one-slot argument to the actual distributed task.
- **Conceptual connection:** Terminal-channel correctness does not determine correctness of an interactive process.
- **Project source:** [Model: accessible ports](../science/model.md#accessible-ports-and-causal-simulation); [resource equivalence: all slots](../science/resource_equivalence.md#simulation-of-all-slots).
- **Wilde pointer:** §§4.4 and 9.5 for channels and their tests; the project and [sequential-simulation comparison](../references/RELATED_WORK.md#entanglement-cost-and-sequential-simulation) supply the causal extension.

### M19

**Control every tester with one resource error**

- **Central question:** Why does a single joint resource approximation control all adaptive experiments without adding errors slot by slot?
- **Target:** Treat the complete simulation and tester as one physical map acting on the initial meter resource and apply purified-distance contractivity.
- **Dependencies and story role:** Uses M09–M10, M16 and M18. It validates correlated resource compression as a causal upper bound.
- **Conceptual connection:** A global state approximation remains global after arbitrary adaptive processing.
- **Project source:** [Resource equivalence: simulation of all slots](../science/resource_equivalence.md#simulation-of-all-slots).
- **Wilde pointer:** §§9.2 and 9.5.

### M20

**Bound the overlap obtainable from a Bell supply**

- **Central question:** How much of a target pure Schmidt spectrum can a state of bounded Schmidt number overlap?
- **Target:** Reconstruct the rank-$`R`$ local-support argument, extend it to mixtures, and apply it to the resource recovered by the tester.
- **Dependencies and story role:** Uses M02, M06–M09 and M17–M18. It proves a converse for arbitrary correlated simulators.
- **Conceptual connection:** A variational eigenvalue bound becomes an operational bound on initial shared entanglement.
- **Project source:** [Bell cost: converse](../science/bell_cost.md#converse).
- **Wilde pointer:** §3.8 and §19.2; the exact overlap argument and Schmidt-number attribution are given in the project.

### M21

**Match the finite-error converse and construction**

- **Central question:** Which retained Schmidt mass is necessary and sufficient for the complete purified-error task?
- **Target:** Combine the converse with deterministic preparation of the normalized truncated resource to obtain the exact smooth-rank Bell-supply formula, including its integer ceiling.
- **Dependencies and story role:** Uses M08–M09 and M19–M20. It establishes the central finite-$`N`$ identity.
- **Conceptual connection:** A state-conversion optimum becomes a chronological process-simulation optimum through both directions of the resource equivalence.
- **Project source:** [Bell cost: rank-tail formula](../science/bell_cost.md#the-rank-tail-formula), including its converse and achievability.
- **Wilde pointer:** §§9.2, 19.3 and 19.4; the project supplies the exact single-experiment result.

### M22

**Evaluate the exact binomial tail**

- **Central question:** How can the minimum Schmidt rank be calculated without listing exponentially many strings?
- **Target:** Order strings by Hamming weight, keep all required lower shells, and count only the needed fraction of the last shell.
- **Dependencies and story role:** Uses M12 and M21. It makes the exact resource formula finite and explicit.
- **Conceptual connection:** Classical type multiplicities describe a quantum Schmidt spectrum, but a whole-shell cutoff can overpay the exact cost.
- **Project source:** [Bell cost: evaluating the rank](../science/bell_cost.md#evaluating-the-rank-without-enumerating-bit-strings).
- **Wilde pointer:** §§14.2–14.4 and 15.1 for probability capture and compression; the partial-shell identity is project-specific.

### M23

**Take the fixed-time Poisson limit, including boundaries**

- **Central question:** Which quantile determines the leading cost when the total duration stays fixed and each slot becomes weak?
- **Target:** Use the parity-of-Poisson coupling to control the binomial quantile, including exact cumulative-probability boundaries, and derive the leading rank and logarithmic coefficient.
- **Dependencies and story role:** Uses M12, M14 and M22. It converts the finite formula into the sharp resolution law.
- **Conceptual connection:** A bounded number of rare events has a growing number of coherent possible positions.
- **Project source:** [Poisson limit: quantile law and boundary coupling](../science/poisson_limit.md#a-sharp-quantile-law), followed by its rank asymptotic.
- **Wilde pointer:** §§10.1, 14.2 and 15.1 for the probability and compression viewpoint; the changing-source Poisson theorem is proved in the project.

### M24

**Keep exact rank, entropy, and fixed-error supply distinct**

- **Central question:** Which resource objective is answered by each of the project's three different asymptotic expressions?
- **Target:** Compare exact Bell supply, exact initial pure-resource entropy or entanglement of formation, and fixed-error Bell supply under their stated quantifiers.
- **Dependencies and story role:** Uses M07–M08, M11 and M21–M23. It prevents an entropy rate from replacing a one-shot resource budget.
- **Conceptual connection:** The same resource state can carry different costs under rank, entropy, and tolerated approximation.
- **Project source:** [Exact resource distinctions](../science/exact_resources.md); [entropy expansion](../science/poisson_limit.md#entropy-supply-and-exact-simulation).
- **Wilde pointer:** §§11.1, 19.2–19.4.

### M25

**Identify what restricted temporal access changes**

- **Central question:** Why can the fixed-pair QND record have bounded cost while a fresh-probe interface has growing cost?
- **Target:** Follow the coherent parity-tagging and final-erasure construction, identify its intermediate-state limitation, and distinguish a fixed offered cadence from a hidden numerical grid.
- **Dependencies and story role:** Uses M05–M06, M15, M18 and M23. It locates the physical interface responsible for the separation.
- **Conceptual connection:** Coherent storage followed by final erasure can restore a final output while leaving intermediate outputs unsuitable for removal.
- **Project source:** [Unraveling gap: input/final data construction](../science/unraveling_gap.md#a-whole-qnd-record-with-no-intermediate-data-access); [fixed physical cadence](../science/continuum_and_cadence.md#what-a-fixed-physical-cadence-changes).
- **Wilde pointer:** §§5.3, 6.2 and 7.2.

### M26

**Specify inefficient readout as a full instrument**

- **Central question:** Which quantum-output task results when the efficient sign is independently corrupted with fixed contrast?
- **Target:** Relate the binary symmetric sign channel, its flip probability, the mixed meter, and the unchanged unread dynamics; distinguish contrast $`\sqrt\zeta`$ from efficiency $`\zeta`$.
- **Dependencies and story role:** Uses M03–M05, M14 and M16. It defines the precise robustness extension.
- **Conceptual connection:** Less information in a record changes conditional backaction and must be represented by completely positive branches.
- **Project source:** [Inefficient record: instrument](../science/inefficient_record.md#the-instrument); [mixed resource recovery](../science/inefficient_record.md#mixed-meter-and-resource-recovery).
- **Wilde pointer:** §§4.2, 4.4 and 4.7.

### M27

**Retain a large entangled sector despite sign noise**

- **Central question:** What shared quantum coherence remains in the one-excitation sector of all archived mixed outputs?
- **Target:** Calculate the sector's success probability and its maximally entangled overlap, and transfer that overlap through one unconditional trace-distance effect.
- **Dependencies and story role:** Uses M02, M10, M17 and M26. It isolates the part of the mixed resource needed for a robust converse.
- **Conceptual connection:** A rare but fixed-probability sector can retain coherence across a dimension growing with the intervention count.
- **Project source:** [Inefficient record: one-excitation sector](../science/inefficient_record.md#the-one-excitation-sector) and [unconditional sector witness](../science/inefficient_record.md#transferring-the-sector-witness-through-a-process-error).
- **Wilde pointer:** §§3.8 and 9.1; §19.2 for its resource role.

### M28

**Prove the inefficient-record logarithmic law**

- **Central question:** How does the retained sector force a growing Bell supply at a fixed small error?
- **Target:** Use the binary relative-entropy estimate and selective LOCC monotonicity for the lower bound, then locally dephase the compressed efficient resource for the uniform upper bound.
- **Dependencies and story role:** Uses M09–M11, M19, M23 and M27. It completes the specified imperfect-detector result.
- **Conceptual connection:** A mixed-state monotone supplies the converse while a contractive resource map supplies the upper, without requiring a sharp mixed-state dilution formula.
- **Project source:** [Inefficient record: entanglement bound](../science/inefficient_record.md#entanglement-required-by-the-successful-state), [upper bound](../science/inefficient_record.md#uniform-upper-bound), and [fixed-time consequence](../science/inefficient_record.md#fixed-time-consequence).
- **Wilde pointer:** §11.8, §19.2 and §9.2.

### M29

**Assemble the scope of each completed resource claim**

- **Central question:** Which source interface, metric, efficiency, error threshold, and order of limits belong to each result?
- **Target:** Give one consistent comparison of efficient purified-error optimality, trace-distance growth, the fixed-positive-efficiency robustness regime, and the free zero-contrast and bounded-cadence cases.
- **Dependencies and story role:** Uses M15 and M18–M28. It checks the scientific conclusion at the complete-task level.
- **Conceptual connection:** A resource law is a statement about an operational task with fixed quantifiers; changing an interface or error convention can change the claim.
- **Project source:** [Model](../science/model.md), [metric comparison](../science/bell_cost.md#a-trace-distance-process-error), [Poisson law](../science/poisson_limit.md#a-sharp-quantile-law), [inefficient fixed-time result](../science/inefficient_record.md#fixed-time-consequence), and [cadence limits](../science/continuum_and_cadence.md#three-different-limits).
- **Wilde pointer:** §§9.1–9.3 and 19.3.

### M30

**Place the result after its inherited ingredients**

- **Central question:** After the known primitives and proof methods are credited, what does this project establish about distributed monitored dynamics?
- **Target:** Connect the known weak meter, sequential resource-seizing framework, Schmidt conversion, and archived-history method to the exact fixed-error resolution law and its specified noisy-record extension; retain the temporal-access and resource qualifications.
- **Dependencies and story role:** Uses the complete narrative M13–M29. It closes the argument from the requested interface to the supported contribution.
- **Conceptual connection:** A familiar construction can support a new operational consequence when its complete task, limiting family, and charged resources are made explicit.
- **Project source:** [Scientific route and central result](../science/README.md), [unraveling separation](../science/unraveling_gap.md#what-the-separation-establishes), and [related work with attribution boundaries](../references/RELATED_WORK.md).
- **Wilde pointer:** §§1.2, 6.1 and 19.3 for the operational resource perspective; the linked scientific account supplies the project's contribution.

