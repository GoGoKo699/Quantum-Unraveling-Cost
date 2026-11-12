# Exact simulation: three different resource questions

[Model](model.md) · [Resource equivalence](resource_equivalence.md) · [Fixed-error Bell supply](bell_cost.md) · [Fixed-time limit](poisson_limit.md)

A weak meter can have small entanglement entropy while still having Schmidt rank two. These facts give different exact simulation costs depending on what the initial resource budget measures. The distinction persists even when the target process is fixed.

Let $`N\geq1`$ and $`0<p<1/2`$. The [resource equivalence](resource_equivalence.md) converts the complete monitored process by LOCC to and from

```math
|\Phi_{N,p}\rangle
=\left(\sqrt{1-p}|00\rangle+\sqrt p|11\rangle\right)^{\otimes N}.
```

All resource dimensions in the optimizations below are finite. Classical randomness, separable auxiliary states, and local memories may be added freely. Every preshared entangled component is included in the actual charged initial resource state. The budgets concern initial supply, with no credit for a resource later returned by the simulator.

## Exact Bell-pair supply

If the initial supply consists of $`m`$ Bell pairs, exact simulation requires

```math
\boxed{C_P^0(N,p)=N.}
```

The resource state $`\Phi_{N,p}`$ has Schmidt rank $`2^N`$, since every one of its squared Schmidt coefficients is positive. The resource-recovering tester converts any exact simulator into exact preparation of this state. An LOCC process started with $`m`$ Bell pairs and separable auxiliaries has Schmidt number at most $`2^m`$, so $`m\geq N`$. Conversely, $`N`$ Bell pairs can be converted by LOCC to the $`N`$ required weak meter pairs, which implement the process exactly.

This is the zero-error case of the [finite-error rank-tail theorem](bell_cost.md). It is a one-shot supply statement. Dividing a standard asymptotic entanglement dilution rate by the number of slots would not establish an exact one-shot preparation protocol.

## Exact initial pure-resource entropy

Now allow an arbitrary finite-dimensional pure shared state $`|\chi\rangle`$ as the initial resource, and charge its entropy of entanglement

```math
E(|\chi\rangle)
=S\!\left(\mathrm{Tr}_B|\chi\rangle\langle\chi|\right).
```

The minimum for exact process simulation is

```math
\boxed{
\inf_{\chi:\,\text{exact simulation}}
E(|\chi\rangle)=Nh_2(p),
}
```

where $`h_2(p)=-p\log_2p-(1-p)\log_2(1-p)`$.

For the upper bound, supply $`|\chi\rangle=|\Phi_{N,p}\rangle`$ and run the exact meter circuit. Its entropy is additive and equals $`Nh_2(p)`$.

For the converse, run the resource-recovering tester after the proposed simulator. It uses only product inputs and LOCC, and its retained output is the pure state $`\Phi_{N,p}`$. Entanglement cannot increase under this deterministic LOCC conversion. More explicitly, entanglement of formation is an LOCC monotone, agrees with entropy of entanglement on pure states, and cannot increase when local residual systems are discarded. Therefore the initial pure-state entropy is at least $`Nh_2(p)`$.

The initial pure resource may have arbitrary correlations across future slots. The proof does not demand a tensor-product resource or assign separate costs to individual meter uses.

## Exact initial entanglement of formation

The same numerical minimum holds when arbitrary mixed finite-dimensional resources $`\sigma_{AB}`$ are allowed and their initial entanglement of formation is charged:

```math
E_F(\sigma_{AB})
=\inf_{\{q_x,\psi_x\}:\,
          \sigma=\sum_xq_x|\psi_x\rangle\langle\psi_x|}
\sum_xq_x
S\!\left(\mathrm{Tr}_B|\psi_x\rangle\langle\psi_x|\right).
```

The exact optimization is

```math
\boxed{
\inf_{\sigma:\,\text{exact simulation}}E_F(\sigma)
=Nh_2(p).
}
```

The pure product of weak meter pairs supplies the upper bound. For any mixed-resource simulator, compose it with the resource-recovering tester and trace out its residual local systems and classical records. This is an LOCC map from the actual initial shared state to $`\Phi_{N,p}`$. Monotonicity gives

```math
E_F(\sigma)\geq E_F(\Phi_{N,p})=Nh_2(p).
```

The argument includes mixtures of resource preparations and public random choices. If a preparation label is retained in local classical registers, those registers are part of the actual initial state when evaluating $`E_F`$. Discarding or hiding the label does not invalidate the converse, because the proof applies directly to whichever state the simulator really receives. Classical outcome records may be retained during the protocol, but the final correction in the recovering tester makes its desired quantum output pure before those records are discarded.

This optimization assigns a value of an entanglement monotone to an initial resource. It does not identify the exact one-shot number of Bell pairs needed to create that resource. In particular, the positive entropy $`Nh_2(p)`$ can be much smaller than its exact Bell-pair supply cost $`N`$.

## Fixed-error Bell supply is a separate question

At allowed purified process error $`0<\varepsilon<1`$, the initial Bell-pair supply is

```math
C_P^{\varepsilon}(N,p)
=\left\lceil\log_2 R_{\varepsilon}(N,p)\right\rceil,
```

with the smooth rank $`R_{\varepsilon}`$ defined in [the exact finite-error theorem](bell_cost.md). A correlated truncated meter state achieves this cost. Thus a simulator need not pay the sum of the exact Bell costs of separate slots when only the complete experiment has a fixed positive error allowance.

For the fixed-time semigroup sequence $`p=p_N=(1-e^{-2\mu/N})/2`$, these distinctions become

| Resource objective | Required initial resource |
| --- | --- |
| Bell pairs, exact process | $`N`$ |
| Arbitrary pure resource, exact process, entropy charged | $`Nh_2(p_N)=\mu\log_2N+\mu\log_2(e/\mu)+o(1)`$ |
| Arbitrary mixed resource, exact process, $`E_F`$ charged | The same $`Nh_2(p_N)`$ |
| Bell pairs, purified process error $`\varepsilon`$ | $`k_{\varepsilon}\log_2N+O_{\mu,\varepsilon}(1)`$ |

The integer Poisson quantile $`k_{\varepsilon}`$ and the zero-cost large-error regime are specified in [the fixed-time limit](poisson_limit.md). The entropy coefficient $`\mu`$ and the one-shot Bell coefficient $`k_{\varepsilon}`$ measure different budgets and need not agree.

## Returned resources and excluded free supplies

The results allow the simulator to retain and reuse its charged local systems, including a correlated shared resource generated from its initial supply. They also allow it to return systems at the end. The stated cost is the initial supply; no subtraction is made for what is returned.

An uncharged entangled catalyst would change the resource model. In particular, an arbitrarily large approximately returned entangled state could supply a resource unavailable from a fixed number of Bell pairs. Neither the Schmidt-number converse nor the monotone budget may be applied after omitting such a state from the initial resource. This is why [the model](model.md) includes every preshared entangled component in the charged supply.

The exact $`E_F`$ statement above is not a general net-consumption theorem for arbitrary correlated returns, and the fixed-error Bell theorem does not assume such a theorem. Its converse uses the complete initial resource and the recoverable quantum output directly.

