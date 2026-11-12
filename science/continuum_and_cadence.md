# Continuous-monitoring interpretation and finite cadence

The resource laws concern exact finite sequences of weak measurement slots. The slot width is $`h=T/N`$, the physical horizon $`T`$ and rate $`\gamma`$ remain fixed, and the available intervention cadence increases with $`N`$. This order of limits is essential.

## Binary slots and the diffusive equation

Write $`Q=Z_A\otimes Z_B`$ and use the instrument of [one generator, different costs](unraveling_gap.md). Its parameters satisfy

```math
p_h=\gamma h+O(h^2),\qquad
\eta_h=2\sqrt{\gamma h}+O(h^{3/2}),
```

and the Kraus expansion is

```math
M_s=\frac1{\sqrt2}
\left[I+s\sqrt{\gamma h}\,Q-\frac{\gamma h}{2}I
+O(h^{3/2})\right].
```

If $`q=\mathrm{Tr}(Q\rho)`$, the probability of $`s`$ is $`(1+s\eta_h q)/2`$. Rescale the measured increment as $`\Delta Y=s\sqrt h`$. Its conditional mean and variance obey

```math
\mathbb E[\Delta Y\mid\rho]
=2\sqrt\gamma\,q h+O(h^2),\qquad
\mathrm{Var}(\Delta Y\mid\rho)=h+O(h^2).
```

Expanding the normalized branch update and separating the innovation $`\Delta W=\Delta Y-\mathbb E[\Delta Y\mid\rho]`$ gives the usual efficient diffusive stochastic master equation

```math
d\rho_t
=\gamma(Q\rho_tQ-\rho_t)\,dt
+\sqrt\gamma\left(Q\rho_t+\rho_tQ
-2\mathrm{Tr}(Q\rho_t)\rho_t\right)dW_t,
```

with observed current

```math
dY_t=2\sqrt\gamma\,\mathrm{Tr}(Q\rho_t)\,dt+dW_t.
```

This is the standard weak-measurement scaling, consistent with quantum-filtering theory; see [Bouten, van Handel and James](https://doi.org/10.1137/060651239). The displayed calculation identifies the limiting drift, innovation and measurement strength. It is not a proof of convergence in a topology that permits an unbounded number of increasingly fast interventions. No such convergence theorem is required for the finite-slot resource bounds, which are exact at each $`N`$.

## Three different limits

The same symbols can conceal different operational questions.

1. **Refine the simulator while holding user access fixed.** A user interacts at only finitely many fixed times. Extra internal subdivision is an implementation choice and does not itself grant the user access to the additional boundaries.
2. **Refine both the record and the intervention interface.** The user may insert a fresh local product probe at every slot and retain all outputs. This is the family priced by the growing-cadence lower bound.
3. **Retain a fixed QND data pair until the end.** Only the classical record is streamed. The one-Bell-pair parity-tagging construction reproduces that record and the final conditional state, independently of internal subdivision.

The second family is stronger than the third. A compression valid only after the whole QND interaction cannot replace a causal simulator whose intermediate data outputs may be removed by the user.

## Why the sparse histories produce logarithmic cost

Let $`\mu=\gamma T`$. For $`N`$ slots,

```math
p_N=\frac{1-e^{-2\mu/N}}2=\frac\mu N+O(N^{-2}).
```

The pure meter resource has Schmidt probabilities indexed by strings $`x\in\{0,1\}^N`$:

```math
\lambda_x=(1-p_N)^{N-|x|}p_N^{|x|}.
```

Most weight sits on a bounded number of excitations, but their possible positions grow with $`N`$. A history of weight $`k`$ has $`\binom Nk`$ possible positions. Capturing a nonzero fraction of one such shell requires rank of order $`N^k`$, and its Bell-pair description costs $`k\log_2N+O(1)`$.

This gives a direct interpretation of the exact smooth-rank law: the entanglement supports a coherent superposition of a bounded number of rare event positions. It is not simply the number of classical record bits, which is $`N`$ for this binary discretization.

The [Poisson theorem](poisson_limit.md) makes this argument exact, including cumulative-probability boundaries. It also identifies the large-error regime in which retaining just the largest Schmidt coefficient suffices and no Bell pair is needed. The rare histories explain the resource; the exact cost and its quantifiers have one authoritative home in that theorem and the [finite-error formula](bell_cost.md).

## What a fixed physical cadence changes

Suppose the interface offers at most a fixed number $`B`$ of weak-measurement slots on $`[0,T]`$, with user interventions only at those boundaries. Then the finite resource laws apply with $`B`$ in place of $`N`$. Refining a hidden numerical integration grid does not replace $`B`$ by a larger physical contact budget. In particular, one Bell pair per offered slot is a finite exact upper bound; the entropy and collective approximate bounds can be smaller.

This observation does not prove a universal bounded-cost theorem for every detector of finite electronic bandwidth. A detector can expose a richer continuous output, internal memory, delays or additional data access. Those features need their own instrument and allowed-tester definition. The established conclusion is narrower: the divergence is controlled by a growing operational time resolution, not by the word “continuous” alone.

The cost model counts initial shared entanglement, while local swaps, protected storage, classical bandwidth and coordination time are free. The lower-bound tester uses $`N`$ local product-probe pairs and archives $`N`$ outputs. Charging those additional resources would be a different complete implementation comparison. The present result isolates the entanglement resource that is absent from unread generator simulation.

## A specified inefficient record

Loss must be modeled as a changed instrument, not only as weaker outcome statistics. For a fixed parameter $`0\le\zeta\le1`$, consider the mixed meter with the same diagonal probabilities $`1-p_h,p_h`$ and off-diagonal coherence $`\sqrt\zeta\sqrt{p_h(1-p_h)}`$ in the correlated basis. The same local controlled-Pauli/readout circuit gives

```math
\mathcal I_s^{(\zeta)}(\rho)
=\frac12\left[(a_hI+s\sqrt\zeta b_hQ)\rho
(a_hI+s\sqrt\zeta b_hQ)
+(1-\zeta)b_h^2 Q\rho Q\right].
```

Its effects are $`(I+s\sqrt\zeta\eta_hQ)/2`$, while summing over $`s`$ gives the same unread channel as before. The diffusive expansion has drift $`\gamma(Q\rho Q-\rho)`$ and innovation coefficient $`\sqrt{\zeta\gamma}`$. Thus $`\zeta`$ is the standard efficiency parameter in this weak-limit description. There is no extra erasure flag exposing which ideal outcomes were lost.

The [inefficient-record analysis](inefficient_record.md) proves a resource bound directly for its mixed outputs. With $`\mu=\gamma T>0`$, every fixed $`\zeta>0`$ still requires $`\Omega(\log N)`$ Bell pairs at any fixed whole-process half-trace error satisfying $`\epsilon<\zeta\mu e^{-\mu}`$. Collective resource truncation supplies $`O(\log N)`$. At $`\zeta=0`$ the record is an independent fair bit and the unread channel is LOCC-free, so the recorded process costs zero entanglement. No sharp coefficient or universal detector model is inferred from these order bounds.
