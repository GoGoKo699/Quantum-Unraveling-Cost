# A bridge from Wilde to remote quantum monitoring

## Exact source and version

The anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge University Press, 2017)**, ISBN 9781107176164, [publisher book DOI](https://doi.org/10.1017/9781316809976). The publisher's [frontmatter and contents](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf) verify the edition and the section/page pointers below. Page numbers in this bridge are the printed 2017 pages.

Wilde's [author page](https://www.markwilde.com/) identifies *From Classical to Quantum Shannon Theory* as the author text associated with this book. The explicitly versioned [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), posted 14 July 2019, is a later corrected draft companion. Its relevant section numbers agree with the printed edition; its pagination differs. It is not silently substituted for the selected edition, and no unversioned “latest” copy supplies the page references here.

## The source map

| Printed second-edition pointer | Tool brought into this project |
|---|---|
| §3.8, “Schmidt Decomposition,” p. 98 | Read a shared pure state's resource spectrum. |
| §§4.2, 4.4 and 4.6, pp. 114, 129 and 143 | Describe a quantum measurement by its conditional maps and its unread channel. |
| §5.3, “Coherent Quantum Instrument,” p. 179 | Keep the quantum output and the measurement record in one physical description. |
| §§6.1–6.2, pp. 186–188 | Treat Bell pairs as a supplied resource and recognize teleportation as a baseline. |
| §§9.1–9.3, pp. 230–253 | Translate distinguishability, fidelity and approximation conventions. |
| §§10.1 and 11.1, pp. 268 and 301 | Distinguish probability entropy from a pure state's entanglement entropy. |
| §§14.2 and 15.1, pp. 408 and 444 | Understand concentration on a small part of a much larger space. |
| §§19.2–19.4, pp. 522–525 | Use LOCC restrictions and entanglement manipulation to price the supplied resource. |

These sections supply the language and standard tools. The shrinking-step Poisson law and its exact finite-error process cost are derived in this repository. They are not presented as textbook theorems.

## First translate the error convention

The [project model](../science/model.md) uses **root fidelity** $`F`$ and purified distance $`P`$:

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1,
\qquad P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}.
```

Wilde's versioned companion §9.2 uses squared fidelity, so its quantity is $`F_{\mathrm W}=F^2`$. The companion §9.1 calls the unhalved norm the trace distance. The project uses half trace distance $`D=\tfrac12\|\rho-\sigma\|_1`$. Thus the conversion is

```math
F_{\mathrm W}=F^2,\qquad
P=\sqrt{1-F_{\mathrm W}},\qquad
\|\rho-\sigma\|_1=2D.
```

For pure states, $`F^2=|\langle\psi|\phi\rangle|^2`$. A retained Schmidt mass $`w`$ therefore gives $`P=\sqrt{1-w}`$, not $`1-w`$. This is why the exact Bell-cost formula uses the mass threshold $`1-\epsilon^2`$.

## From a channel to a recorded instrument

Put one data qubit in each lab and write $`Q=Z_A\otimes Z_B`$. One slot has two conditional maps, labeled by $`s=\pm1`$:

```math
\mathcal I_s(\rho)=M_s\rho M_s^\dagger,
\qquad M_s=\frac{\sqrt{1-p}\,I+s\sqrt p\,Q}{\sqrt2}.
```

Its unread channel is obtained by summing the two maps. That sum is $`(1-p)\rho+pQ\rho Q`$, which Alice and Bob can implement using shared randomness and their local $`Z`$ gates. The record instead identifies which coherent sum of $`I`$ and $`Q`$ acted. The distinction is between two physical interfaces, even though their unread evolution agrees.

Book §§4.2 and 4.6 make it natural to include the classical sign register in the output state. In this project that register cannot be discarded before evaluating the monitored process. A simulator also has to return the quantum data after each slot, because the user may remove it before the next interaction.

## From a product probe to a resource spectrum

Feed the product input $`|++\rangle`$. Either sign occurs with probability one half. After an outcome-dependent local correction, both branches yield

```math
|\phi_p\rangle
=\sqrt{1-p}|++\rangle+\sqrt p|--\rangle.
```

The Schmidt probabilities are $`1-p,p`$. A fresh product input in every slot, with every output saved, produces $`|\phi_p\rangle^{\otimes N}`$. No entangled tester input is needed for this converse.

Conversely, the known weak-meter circuit uses one copy of this same shared resource per slot to implement the instrument on every input. The two directions identify the complete process with its tensor-meter resource for the entanglement account. The construction is credited to the primary literature in [related work](../references/RELATED_WORK.md); the [resource-equivalence proof](../science/resource_equivalence.md) states the causal reduction.

## From entanglement manipulation to one joint truncation

A supply of $`m`$ Bell pairs has Schmidt rank $`2^m`$. Local operations and classical communication cannot make a state of larger Schmidt number from that supply and separable local inputs. Therefore a simulator cannot approximate the archived pure target more closely than the mass captured by its largest $`2^m`$ Schmidt probabilities.

For the upper bound, retain the smallest number $`R_\epsilon`$ of target Schmidt terms whose total mass is at least $`1-\epsilon^2`$. Normalize the truncated vector. It can be prepared from $`\lceil\log_2R_\epsilon\rceil`$ Bell pairs by the standard pure-state conversion theorem, and its purified distance to the full resource is at most $`\epsilon`$.

Why does this approximate **every** intervened experiment? Fix any user strategy. The local meter circuit together with all that strategy's operations is one quantum channel acting on the initial resource. Fidelity is nondecreasing under that channel, so purified distance cannot increase. The same resource approximation therefore controls every strategy with the same total error. There is no sum of $`N`$ independently assigned error tolerances. The [Bell-cost proof](../science/bell_cost.md) makes this argument precise.

Chapter 19's fixed-source asymptotic entanglement rate is helpful background, but it does not by itself give this finite-rank formula. Likewise, entropy $`N h_2(p)`$ and the exact integer Bell count $`N`$ answer different questions.

## Why typicality changes into a Poisson problem

For the monitoring family, $`p=p_N=(1-e^{-2\mu/N})/2`$ with fixed $`\mu=\gamma T`$. The source becomes weaker as the number of slots grows. Its Schmidt labels have a binomial number of rare excitations tending to a Poisson distribution, rather than a fixed-distribution typical fraction.

For any fixed retained error, only finitely many excitations are needed, but choosing their positions can require a rank growing as a power of $`N`$. The logarithm of that rank gives the logarithmic Bell cost. This is developed in the [Poisson law](../science/poisson_limit.md). It is a project-specific triangular-array argument, not a direct use of a fixed-source coding rate.

For the specified inefficient detector, the resource becomes mixed and the exact pure-state spectrum formula no longer applies unchanged. The [inefficient-record analysis](../science/inefficient_record.md) instead extracts a locally flagged entangled sector and applies a relative-entropy bound. This connects naturally to §§11.8 and 19.2 while keeping the changed instrument explicit.

Continue with the [two-slot example](WORKED_EXAMPLE.md), then the [milestone route](MILESTONES.md). The [unraveling comparison](../science/unraveling_gap.md) explains why neither the free unread channel nor the constant-cost final-only QND record invalidates the intervened-process law.
