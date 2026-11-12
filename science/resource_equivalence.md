# The monitored process and its entangled resource

[Model and conventions](model.md) · [Bell-pair cost](bell_cost.md) · [Fixed-time limit](poisson_limit.md)

The complete monitored process has an exact two-way conversion to a known pure entangled state using local operations and classical communication (LOCC). One conversion implements the measurement; the other recovers the resource from the measurement outputs. This gives a converse against correlated simulators and a uniform upper bound for adaptive inputs.

The one-step weak meter is an established construction; the [related-work account](../references/RELATED_WORK.md) identifies the nonlocal-measurement and channel-simulation antecedents. The argument below states the conversion explicitly so that its causal and resource assumptions remain visible.

## One slot

Alice and Bob each hold one data qubit. Let $`Q=Z_A\otimes Z_B`$, and let $`0\leq p\leq 1/2`$. The two-outcome instrument has a public sign $`r\in\{+1,-1\}`$ and Kraus operator

```math
M_r(p)=\frac{\sqrt{1-p}\,I+r\sqrt p\,Q}{\sqrt2}.
```

Its effects and unread channel are

```math
M_r(p)^\dagger M_r(p)
=\frac{I+r\eta Q}{2},
\qquad \eta=2\sqrt{p(1-p)},
```

```math
\sum_{r=\pm1}M_r(p)\rho M_r(p)^\dagger
=(1-p)\rho+pQ\rho Q.
```

The Kraus operators are positive for the specified range of $`p`$. Thus this is the Lüders instrument of the displayed effects. Its conditional quantum output, including coherence within and between parity sectors, is part of the task.

Define the normalized meter state

```math
|\phi_p\rangle
=\sqrt{1-p}\,|00\rangle+\sqrt p\,|11\rangle.
```

One copy is shared between the two laboratories. Each party applies a controlled $`Z`$ from its meter qubit to its data qubit and measures its meter in the $`X`$ basis. Write the two local signs as $`s_A,s_B\in\{+1,-1\}`$. The resulting data Kraus operator is

```math
K_{s_A,s_B}
=\frac{\sqrt{1-p}\,I+s_As_B\sqrt p\,Q}{2}
=\frac{M_{s_As_B}(p)}{\sqrt2}.
```

There are two local sign pairs with each product $`r=s_As_B`$. Reporting their product and discarding the extra local random bit therefore implements exactly the target instrument. The calculation is an operator identity, so it applies to arbitrary mixed data and arbitrary reference correlations.

## Simulation of all slots

Let $`\mathcal C_{N,p}`$ denote the chronological process consisting of $`N`$ copies of this instrument, with its data ports and record accessible at every slot as specified in [the model](model.md). The slots admit arbitrary causal interventions. Data supplied later may depend on earlier records and may be entangled with retained systems.

Prepare the joint resource

```math
|\Phi_{N,p}\rangle=|\phi_p\rangle^{\otimes N},
```

and use one meter pair at each slot. The preceding operator identity proves exact simulation of $`\mathcal C_{N,p}`$ by a causal LOCC circuit.

The same circuit also accepts an arbitrary replacement resource $`\sigma`$ on the joint meter space. Its slot marginals need not be independent: a correlated replacement generally induces correlations across the simulated slots. For every causal tester $`\mathcal T`$, the entire experiment, including its retained reference and record, is a completely positive trace-preserving map $`\Lambda_{\mathcal T}`$ acting on the initial resource. Consequently,

```math
P\!\left(\mathcal T[\mathcal C_{N,p}],
          \mathcal T[\widetilde{\mathcal C}_{\sigma}]\right)
\leq P\!\left(\Phi_{N,p},\sigma\right).
```

Here $`F`$ is root fidelity and $`P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}`$ is purified distance. Taking the supremum over testers gives

```math
d_P\!\left(\mathcal C_{N,p},
             \widetilde{\mathcal C}_{\sigma}\right)
\leq P\!\left(\Phi_{N,p},\sigma\right).
```

This is a bound on the complete adaptive experiment. It does not distribute an error allowance across the individual slots and does not use a per-slot union bound.

## Recovering the resource from the process

There is also an LOCC tester that converts $`\mathcal C_{N,p}`$ into $`\Phi_{N,p}`$. At each slot, supply the fresh product state $`|+\rangle_A|+\rangle_B`$, retain its quantum output, and use new data qubits at the next slot. Both signs occur with probability $`1/2`$, and the normalized output is

```math
|\psi_r\rangle
=\sqrt{1-p}\,|++\rangle+r\sqrt p\,|--\rangle.
```

When $`r=-1`$, Alice applies $`X_A`$. It leaves $`|++\rangle`$ unchanged and reverses the sign of $`|--\rangle`$. Both parties then apply a Hadamard gate. The corrected output is $`|\phi_p\rangle`$ for either sign. After this correction the classical sign can be discarded without mixing the resource state.

Repeating with fresh product inputs yields exactly $`\Phi_{N,p}`$. No initial entanglement is supplied by this tester. Its required operations are local input preparation, output archiving, local corrections, and classical communication of the record.

If a simulator has uniform process error at most $`\varepsilon`$, the same tester yields a state $`\rho`$ satisfying

```math
P\!\left(\rho,\Phi_{N,p}\right)\leq\varepsilon.
```

Any residual simulator memory is discarded in this statement. Discarding it is an allowed local operation and cannot create the bipartite entanglement used in the converse.

## Operational consequence

The target process and the pure state $`\Phi_{N,p}`$ are exactly interconvertible by LOCC. Thus any charged resource sufficient for process simulation must also suffice for approximate preparation of this state. Conversely, an approximate preparation of this state gives a simulator with at most the same purified error against every causal tester.

The two directions hold for complete chronological experiments. In particular, the converse does not assume that the simulator uses independent meters or that it consumes a separately identifiable amount of entanglement at each slot. It allows charged correlated resources, adaptive local processing, and reuse of its local memories. The [Bell-pair theorem](bell_cost.md) applies this equivalence to a specified initial resource supply.

The ability to retain quantum outputs between slots is essential. A model that gives users only a final quantum output, or only a classical record, is a different task; the [unraveling comparison](unraveling_gap.md) makes these distinctions explicit.

