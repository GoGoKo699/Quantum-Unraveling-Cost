# Related work and attribution

The contribution is a time-resolution law for the distributed implementation of a specified monitored process. Its ingredients include established nonlocal weak measurements, sequential channel simulation, entanglement monotones and pure-state conversion. The bibliography is in [references.bib](references.bib). The comparison below separates those ingredients from the result established here.

## Efficient nonlocal weak measurements

[Pierre Vidil and Keiichi Edamatsu, *Nonlocal generalized quantum measurements of bipartite spin products without maximal entanglement*, New Journal of Physics 23, 043004 (2021)](https://doi.org/10.1088/1367-2630/abee3f); [arXiv:1912.07135v1](https://arxiv.org/abs/1912.07135v1).

Their Sections III and VI construct an arbitrary-strength spin-product measurement using a nonmaximally entangled meter and identify the relation between measurement strength and meter concurrence. The controlled-Pauli/X-readout primitive in this repository is a local-basis version of that construction. Its efficient branch backaction and one-step meter/strength relation are inherited. The new cost statement must therefore concern the complete shrinking-step family, collective fixed-error compression, and the temporal access offered to the tester; it is not a new nonlocal weak-measurement primitive.

[Aharon Brodutch and Eliahu Cohen, *Nonlocal Measurements via Quantum Erasure*, Physical Review Letters 116, 070404 (2016)](https://doi.org/10.1103/PhysRevLett.116.070404); [arXiv:1409.1575](https://arxiv.org/abs/1409.1575).

This earlier work realizes nonlocal product-observable interactions with adjustable strength through quantum erasure. It establishes the feasibility of weak and intermediate-strength nonlocal measurements. Here unlimited classical coordination is allowed, and the task is the entanglement cost of reproducing a causal recorded instrument. No claim of a new erasure principle or instantaneous spacelike measurement is made.

[Lan Jiang, Zhenhua Li and Tao Li, *Nonlocal generalized quantum measurement of product observables with mixed entanglement*, Optics Express 31, 12508–12519 (2023)](https://doi.org/10.1364/OE.487883).

This work uses mixed entangled meters for arbitrary-strength product-observable measurements. It is a relevant resource comparison, but a measurement's outcome probabilities do not by themselves determine its disturbance. The efficient Lüders instrument here has a single Kraus operator in each retained branch. An allegedly cheaper simulator must reproduce that backaction on arbitrary reference-entangled inputs, not only the same POVM. The [inefficient-record account](../science/inefficient_record.md) states a particular mixed-meter extension and proves its fixed-small-error logarithmic supply bound. Its primitive is a local dephasing of the known pure meter; the new claim concerns uniform process cost with growing temporal access. Other mixed-branch variants require separate bounds.

## Entanglement cost and sequential simulation

[Somshubhro Bandyopadhyay, Gilles Brassard, Shelby Kimmel and William K. Wootters, *Entanglement cost of nonlocal measurements*, Physical Review A 80, 012313 (2009)](https://doi.org/10.1103/PhysRevA.80.012313); [arXiv:0809.2264](https://arxiv.org/abs/0809.2264).

Entanglement production as a lower bound on nonlocal-measurement cost is established methodology. Here the fresh-product-probe test turns every retained weak-measurement branch into a known pure entangled pair. Its use is an application of that methodology, not a new monotonicity principle.

[Stefan Bäuml, Siddhartha Das, Xin Wang and Mark M. Wilde, *Resource theory of entanglement for bipartite quantum channels*, arXiv:1907.04181v1 (2019)](https://arxiv.org/abs/1907.04181v1).

Section 3.1 defines sequential simulation against adaptive strategy tests and resource-seizable bidirectional channels. Theorem 1 reduces their sequential entanglement cost to the underlying resource state's cost. It also explains why an approximation to a joint resource state controls every adaptive simulation test. The efficient parity instrument is resource-seizable: a local product input and outcome-dependent local correction recover its pure meter state. These general simulation and reduction principles are inherited.

The fixed-channel many-copy asymptotic theorem does not state the present triangular family, where the channel itself weakens as $`p_N\sim\mu/N`$. Here its structure is used to derive the exact finite-$`N`$ Bell cost in purified strategy distance from the captured Schmidt mass, and then the Poisson-quantile coefficient of $`\log N`$. The zero-cost unread/jump interface and bounded-cost no-intervention QND interface specify what operationally changes when the time-resolved efficient instrument is requested.

[Michael A. Nielsen, *Conditions for a Class of Entanglement Transformations*, Physical Review Letters 83, 436–439 (1999)](https://doi.org/10.1103/PhysRevLett.83.436), supplies deterministic pure-state conversion by majorization. [Barbara M. Terhal and Paweł Horodecki, *Schmidt number for density matrices*, Physical Review A 61, 040301(R) (2000)](https://doi.org/10.1103/PhysRevA.61.040301), supplies LOCC monotonicity of Schmidt number. These results support the resource truncation upper bound and the Bell-rank converse.

## Continuous measurements and their costs

[Lorena Ballesteros Ferraz and Cyril Elouard, *Weak continuous measurements require more work than strong ones*, Physical Review Research 8, 013305 (2026)](https://doi.org/10.1103/6p2c-nbg5); [arXiv:2502.09732v4](https://arxiv.org/abs/2502.09732v4), revised 15 June 2026.

This is a direct conceptual antecedent to the observation that a sequence of increasingly weak measurements can be more costly than a single strong measurement. Its resource is thermodynamic work in an apparatus model that includes objectification and reset. The present resource is initial shared entanglement under LOCC simulation, with a uniform error criterion for intervened quantum data and its retained record. The distinction is consequential: the same unread generator here is exactly LOCC-free, and the whole fixed-pair QND record has constant entanglement cost when intermediate data access is absent. The present result is not the first observation that “weak can cost more.”

[Luc Bouten, Ramon van Handel and Matthew R. James, *An Introduction to Quantum Filtering*, SIAM Journal on Control and Optimization 46, 2199–2241 (2007)](https://doi.org/10.1137/060651239); [arXiv:math/0601741](https://arxiv.org/abs/math/0601741).

Quantum filtering supplies the standard diffusive and jump descriptions used to interpret the binary weak slots. The infinitesimal expansion in [continuum and cadence](../science/continuum_and_cadence.md) identifies the usual efficient parity-monitoring equation. The resource theorem is proved at finite slot number; no convergence theorem uniform over an unbounded number of increasingly fast interventions is claimed.

## An archived-history converse for an autonomous bath

[Autonomous Markovian Noise, “A finite bath needs logarithmic memory”](https://github.com/GoGoKo699/Autonomous-Markovian-Noise/blob/3d743d7a740fff773b9b95a4bbc4f3a2afcc3785/science/memory_bound.md), source revision $`3d743d7a740fff773b9b95a4bbc4f3a2afcc3785`$.

That public account uses swaps with fresh probes, archival quantum memory and spectral weight to prove a finite-bath dimension obstruction for autonomous dephasing under interventions. This repository reuses the idea of retaining many weak outputs rather than testing only an endpoint. The resource and model differ: the bath result constrains the dimension of a closed environment under joint unitary evolution; the present result permits LOCC, discards, classical communication and mixed initial resources while pricing shared entanglement for a particular efficient unraveling. A bath rank bound alone does not establish that entanglement cost, and the unread dynamics here needs no entanglement at all.

## Scope of the literature comparison

Primary model and theorem statements were inspected for the material comparisons above. The account credits known primitives and general methods and identifies the additional finite-resolution result. It does not certify exhaustive priority over every continuous-measurement, channel-simulation or distributed-control paper. In particular, generating entanglement conditionally when unconditional dynamics is separable is a familiar phenomenon; the result here is its quantitative causal implementation cost with explicit temporal access and error conventions.
