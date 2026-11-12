# Remote monitoring and its resource account

[Science route](README.md) · [Resource equivalence](resource_equivalence.md) · [Exact Bell cost](bell_cost.md)

Alice and Bob hold one data qubit each. Their common environment implements parity dephasing. Reading that environment in different bases produces different measurement records, called unravelings. We ask how many initially shared Bell pairs are needed to reproduce the complete recorded experiment when the users may intervene between weak measurement steps.

## Fixed-time family

Write $`Q=Z_A\otimes Z_B`$. Fix $`\gamma,T\gt0`$, let $`\mu=\gamma T`$, and divide the duration into $`N\ge1`$ slots of length $`\delta=T/N`$. Set

```math
p_N=\frac{1-e^{-2\mu/N}}2,\qquad
a_N=\sqrt{1-p_N},\qquad b_N=\sqrt{p_N}.
```

One slot returns a classical sign $`s\in\{+1,-1\}`$ and the quantum output of the efficient instrument

```math
\mathcal I_s(\rho)=M_s\rho M_s^\dagger,
\qquad
M_s=\frac{a_N I+s b_N Q}{\sqrt2}.
```

These are positive Kraus operators, so this is the Lüders instrument of

```math
M_s^\dagger M_s=\frac{I+s\eta_NQ}{2},
\qquad \eta_N=2a_Nb_N=\sqrt{1-e^{-4\mu/N}}.
```

The small Schmidt probability $`p_N`$ is of order $`\delta`$; the measurement strength $`\eta_N`$ is of order $`\sqrt\delta`$. They are different parameters. Ignoring the sign gives exactly

```math
\mathcal E_\delta(\rho)
=(1-p_N)\rho+p_NQ\rho Q
=e^{\delta\mathcal L}(\rho),
\qquad
\mathcal L(\rho)=\gamma(Q\rho Q-\rho).
```

## Accessible ports and causal simulation

After each slot the quantum output and classical sign are accessible before the next slot starts. A user may apply arbitrary local instruments, keep protected local quantum memories and references, prepare fresh local input qubits, swap them into the ports, and choose subsequent operations using previous records. There are $`N`$ instrument calls and $`N-1`$ interior boundaries. The simulator must respect that order. A terminal-only channel approximation is insufficient.

The target is the complete $`N`$-slot causal process $`\mathsf C_{N,p}`$, with $`p=p_N`$ unless otherwise specified. Its signs are available to both parties by free classical communication. A tester is trace preserving: any heralded branch and its failure flag remain part of the unconditional final state. Its final quantum output includes the retained classical record. Arbitrary finite local memories are allowed. Taking the supremum over all causal quantum testers, including stronger testers with global reference processing, gives the same resource bounds: the upper holds for that larger class, and the converse uses only fresh local product inputs and local swaps.

## Initially supplied entanglement

A simulator starts with exactly $`m`$ Bell pairs, local ancillas, and shared classical randomness independent of the inputs. It may use arbitrary finite-dimensional LOCC, correlated resources obtained from those Bell pairs, local discards, and reuse across slots. Local gates, memory, preparation, measurement and classical communication are free. Quantum communication is absent. The cost is the deterministic initial Bell-pair supply, including pairs kept as catalysts or left unused. There is no free entangled catalyst and no postselected or average budget convention.

This deliberately favorable local resource account isolates shared entanglement. It does not give a gate, memory, energy, latency or hardware cost optimum. In particular, free classical communication is not a finite-speed spacetime implementation model.

For two normalized states, use root fidelity and purified distance

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1,
\qquad
P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}.
```

For processes define

```math
d_P(\mathsf C,\mathsf D)
=\sup_{\mathsf T}P\bigl(\mathsf T[\mathsf C],\mathsf T[\mathsf D]\bigr),
\qquad
C_P^\epsilon(N,p)
=\min\{m:\ d_P(\mathsf C_{N,p},\mathsf S_m)\le\epsilon\}.
```

The minimum is over causal LOCC simulators with the stated initial supply. We use $`0\le\epsilon\lt1`$. A separate half-trace-distance criterion uses

```math
d_T(\mathsf C,\mathsf D)
=\sup_{\mathsf T}\frac12\|\mathsf T[\mathsf C]-\mathsf T[\mathsf D]\|_1.
```

The error is for the whole experiment, uniformly over interventions, with fixed total tolerance as $`N`$ grows. The exact finite cost formula belongs to $`d_P`$. The [Bell-cost proof](bell_cost.md) translates the conclusions to $`d_T`$ without identifying their finite-error optima.

## Other resource conventions

The [exact-resource account](exact_resources.md) also minimizes initial entanglement of formation over arbitrary finite-dimensional shared states for an exact simulation. On pure states that quantity is the entropy of one share. This gives $`N h_2(p)`$, while the exact initial Bell-pair number is $`N`$. Neither quantity is a net catalytic-consumption rate or a thermodynamic work cost.

## Scope of the limiting statement

The asymptotic variable is the intervention resolution $`N`$, with $`\mu`$ and total error fixed. The target is this specified weak-step family. The [continuum and cadence account](continuum_and_cadence.md) explains its connection to diffusive monitoring and why it does not prove an infinite cost for a monitor with a fixed accessible bandwidth. The [inefficient-record theorem](inefficient_record.md) specifies and solves a binary symmetric readout-noise extension at the level of logarithmic growth. Other detector errors, noisy local memories and finite-speed feedback require their own output and error models.
