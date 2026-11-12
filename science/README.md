# The scientific account

The monitored environment is part of a distributed task. Two records can describe the same unread noise while requiring different shared quantum resources. This project makes that distinction quantitative for parity dephasing at fixed duration.

Read the [model](model.md) first. The proof then has two parts: recover a known pure resource from the entire monitored process, and calculate the least Bell supply that approximates that resource. Both directions include the complete causal interface.

| Question | Authoritative account |
|---|---|
| What is available, charged and compared? | [Model and error](model.md) |
| Why do correlated meters and reuse not improve the optimum? | [Exact resource/process equivalence](resource_equivalence.md) |
| What is the minimum finite-error Bell supply? | [Smooth-rank formula](bell_cost.md) |
| How does a fixed duration produce a Poisson law? | [Resolution asymptotics](poisson_limit.md) |
| Why do entropy supply and exact Bell count differ? | [Exact resource conventions](exact_resources.md) |
| How can the same noise have free and costly records? | [Unraveling separation](unraveling_gap.md) |
| Does specified inefficient readout remove the cost? | [Noisy-record robustness](inefficient_record.md) |
| What happens when access has finite cadence? | [Continuum interpretation and interface limits](continuum_and_cadence.md) |
| Which ingredients are established work? | [Related work](../references/RELATED_WORK.md) |
| What finite checks can be reproduced? | [Verification](../verification/README.md) |

The main finite statement is an exact one-shot identity. Let $`\lambda_1\ge\lambda_2\ge\cdots`$ be the squared Schmidt coefficients of

```math
|\phi_p\rangle^{\otimes N},
\qquad |\phi_p\rangle=\sqrt{1-p}|00\rangle+\sqrt p|11\rangle.
```

Then

```math
C_P^\epsilon(N,p)
=\left\lceil\log_2\min\left\{R:\sum_{j=1}^R\lambda_j\ge1-\epsilon^2\right\}\right\rceil.
```

At $`p=p_N`$ and fixed $`\mu,\epsilon`$, the [Poisson theorem](poisson_limit.md) evaluates its leading order. The coefficient is a one-experiment quantile, rather than an entropy rate. The [unraveling comparison](unraveling_gap.md) places this cost beside exactly free unread and jump-record implementations. All statements retain the resource and interface qualifications in the model.
