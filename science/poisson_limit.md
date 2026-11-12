# Fixed time and increasing intervention bandwidth

[Model](model.md) · [Exact finite-error Bell cost](bell_cost.md) · [Exact resource distinctions](exact_resources.md) · [Unravelings](unraveling_gap.md)

Fix a positive monitoring strength $`\gamma`$ and physical duration $`T`$. Let $`\mu=\gamma T>0`$, and split this duration into $`N`$ intervention slots. The exact parity-dephasing semigroup determines

```math
p_N=\frac{1-e^{-2\mu/N}}{2},
\qquad Np_N\longrightarrow\mu.
```

The corresponding Lüders measurement strength is $`\eta_N=2\sqrt{p_N(1-p_N)}=\sqrt{1-e^{-4\mu/N}}`$. It scales as $`N^{-1/2}`$, while the small Schmidt probability $`p_N`$ scales as $`N^{-1}`$.

The result below holds for one complete fixed-time experiment with a fixed allowed total error. It is a different limiting regime from taking many independent copies of one fixed instrument and then letting their joint error vanish.

## A sharp quantile law

For fixed $`0<\varepsilon<1`$, let

```math
a=1-\varepsilon^2,
\qquad
k_{\varepsilon}
=\min\{k\geq0:\Pr(K\leq k)\geq a\},
\qquad K\sim\mathrm{Pois}(\mu).
```

Then the minimum initial Bell-pair supply under uniform purified process error satisfies

```math
\boxed{
C_P^{\varepsilon}(N,p_N)
=k_{\varepsilon}\log_2N+O_{\mu,\varepsilon}(1).
}
```

The statement includes errors for which $`a`$ is exactly a Poisson cumulative probability. No exclusion of those boundary values is needed for this semigroup discretization.

If $`k_{\varepsilon}=0`$, the stronger conclusion is

```math
C_P^{\varepsilon}(N,p_N)=0
\quad\text{for every }N.
```

This occurs precisely when $`\varepsilon^2\geq1-e^{-\mu}`$. In the complementary regime $`\varepsilon^2<1-e^{-\mu}`$, the coefficient is a positive integer and the required supply grows as $`\Theta_{\mu,\varepsilon}(\log N)`$.

## Why the Poisson boundary is controlled

Let $`X_1,\ldots,X_N`$ be independent Poisson variables of mean $`\mu/N`$, and set $`Y_i=X_i\bmod2`$. The probability of an odd Poisson count is

```math
\Pr(Y_i=1)
=\frac{1-\mathbb E[(-1)^{X_i}]}2
=\frac{1-e^{-2\mu/N}}2=p_N.
```

Hence $`S_N=\sum_iY_i`$ has distribution $`\mathrm{Bin}(N,p_N)`$, while $`\sum_iX_i`$ has distribution $`\mathrm{Pois}(\mu)`$. The coupling satisfies $`S_N\leq\sum_iX_i`$ pointwise. Therefore, for every integer $`k`$,

```math
F_N(k):=\Pr(S_N\leq k)
\geq F_{\mu}(k):=\Pr(K\leq k).
```

Also $`S_N`$ converges in distribution to $`K`$, since $`p_N\to0`$ and $`Np_N\to\mu`$. For fixed $`k`$, this gives $`F_N(k)\to F_{\mu}(k)`$.

By definition of $`k_{\varepsilon}`$,

```math
F_{\mu}(k_{\varepsilon}-1)<a
\leq F_{\mu}(k_{\varepsilon}).
```

The lower strict inequality and convergence show that $`F_N(k_{\varepsilon}-1)<a`$ for all sufficiently large $`N`$. The coupling gives $`F_N(k_{\varepsilon})\geq a`$ for every $`N`$, even when the upper inequality is equality. Consequently, the finite binomial quantile in the [rank-tail formula](bell_cost.md#evaluating-the-rank-without-enumerating-bit-strings) obeys

```math
k_N=k_{\varepsilon}
\quad\text{for all sufficiently large }N.
```

This argument uses the exact value of $`p_N`$. A statement for an arbitrary sequence satisfying only $`Np_N\to\mu`$ would need a separate treatment of boundary values.

## From the quantile to the Schmidt rank

Suppose $`k=k_{\varepsilon}\geq1`$. Let

```math
r=a-F_{\mu}(k-1)>0.
```

The probability of any one Schmidt string in shell $`k`$ obeys

```math
w_{k,N}=(1-p_N)^{N-k}p_N^k
\sim e^{-\mu}\mu^k N^{-k}.
```

The numerator of the partial last shell tends to $`r`$. The complete lower shells contain only $`O(N^{k-1})`$ strings. It follows from the exact partial-shell formula that

```math
R_{\varepsilon}(N,p_N)
\sim \frac{r e^{\mu}}{\mu^k}\,N^k.
```

Taking logarithms and then the Bell-pair ceiling proves the quantile law. At an upper-CDF boundary $`a=F_{\mu}(k)`$, one has $`r=e^{-\mu}\mu^k/k!`$, and the displayed leading rank is $`N^k/k!`$. Thus this boundary retains the same integer coefficient $`k`$.

For $`k=0`$, the coupling gives $`(1-p_N)^N=F_N(0)\geq e^{-\mu}\geq a`$. One Schmidt coefficient already retains the required probability, so $`R_{\varepsilon}=1`$ for every $`N`$.

## Example

Take $`\mu=1`$ and purified process error $`\varepsilon=0.1`$, so the required retained probability is $`0.99`$. The Poisson cumulative probabilities at three and four are approximately $`0.9810`$ and $`0.9963`$. Hence

```math
k_{0.1}=4,
\qquad C_P^{0.1}(N,p_N)=4\log_2N+O(1).
```

The coefficient is a quantile, rather than the mean number $`\mu`$ of rare meter excitations. This distinction matters when pricing the initial supply for a single experiment at a specified global confidence level.

## Entropy supply and exact simulation

The exact minimum initial pure-resource entropy, and the exact minimum initial entanglement of formation, are each $`Nh_2(p_N)`$, as proved in [exact resource distinctions](exact_resources.md). Their expansion is

```math
Nh_2(p_N)
=\mu\log_2N+\mu\log_2(e/\mu)+o(1).
```

Indeed $`p_N=\mu/N-\mu^2/N^2+O(N^{-3})`$, and $`h_2(p)=p\log_2(1/p)+p\log_2e+O(p^2)`$. Multiplication by $`N`$ gives the displayed expression.

This entropy coefficient $`\mu`$ need not equal the one-shot Bell-supply coefficient $`k_{\varepsilon}`$. At zero allowed error the Bell-pair supply is instead exactly $`N`$, because every Schmidt probability is positive. The limits $`N\to\infty`$ at fixed positive error and $`\varepsilon\to0`$ are therefore distinct.

## Trace-distance error

The [metric comparison](bell_cost.md#a-trace-distance-process-error) yields

```math
C_P^{\sqrt{2\varepsilon}}(N,p_N)
\leq C_T^{\varepsilon}(N,p_N)
\leq C_P^{\varepsilon}(N,p_N).
```

In particular, for fixed $`\mu>0`$ and $`0<\varepsilon<(1-e^{-\mu})/2`$, both bounds have a positive finite logarithmic coefficient. Thus

```math
C_T^{\varepsilon}(N,p_N)=\Theta_{\mu,\varepsilon}(\log N).
```

The sharp coefficient derived here belongs to purified process error. The trace-distance inequalities establish the growth order and do not identify its exact coefficient.

## Physical scope

Increasing $`N/T`$ increases the rate at which users can replace the monitored data and retain earlier quantum outputs. The result prices a distributed interface that must remain correct under those interventions. It does not follow merely from requesting a more finely digitized classical record of two uninterrupted qubits.

The comparison with the zero-entanglement jump record of the same unread semigroup, and with the bounded resource needed without intermediate access, is given in [unravelings](unraveling_gap.md). Local gates, classical records, storage, latency, and energetic reset costs are outside this resource objective.

