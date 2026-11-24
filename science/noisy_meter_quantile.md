# The Bell-pair coefficient for an inefficient record

[Model](model.md) · [Inefficient instrument and mixed meters](inefficient_record.md) · [Efficient-record cost](bell_cost.md) · [Related work](../references/RELATED_WORK.md)

Independent errors in the binary record reduce the leading Bell-pair cost of simulating the whole monitored experiment. At fixed error in purified distance, the cost is set by a Poisson quantile with mean $`\zeta\mu`$, where $`\zeta`$ is the detector efficiency and $`\mu=\gamma T`$ is fixed by the unread dephasing. The cost changes in integer steps as the efficiency or error tolerance varies.

## Statement and resource convention

Let $`\mu\gt 0`$, $`0\lt \zeta\leq1`$, and $`0\lt\varepsilon\lt1`$ be fixed, and set $`p_N=(1-e^{-2\mu/N})/2`$. The sign is independently flipped with probability $`(1-\sqrt\zeta)/2`$ in each slot. The noisy signs and quantum outputs remain available for interventions between slots. Let $`C_{P,\zeta}^{\varepsilon}(N,p_N)`$ be the minimum deterministic initial supply of Bell pairs under the [whole-process purified distance](model.md#initially-supplied-entanglement), with arbitrary causal LOCC and no quantum communication or free shared entanglement. Write

```math
k=\min\bigl\{j\in\mathbb Z_{\geq0}:\Pr[X\gt j]\leq\varepsilon^2\bigr\},
\qquad X\sim\mathrm{Pois}(\zeta\mu).
```

Then

```math
\boxed{C_{P,\zeta}^{\varepsilon}(N,p_N)
       =k\log_2 N+O_{\mu,\zeta,\varepsilon}(1).}
```

The coefficient uses the displayed weak inequality, including when $`\Pr[X\gt k]=\varepsilon^2`$. If $`\varepsilon^2\geq 1-e^{-\zeta\mu}`$, zero Bell pairs suffice at every $`N`$. At $`\zeta=0`$, the independent fair record and unread evolution have an exact zero-Bell implementation at every $`N`$.

The result keeps $`\mu,\zeta,\varepsilon`$ fixed as $`N`$ grows. The companion account gives [finite-resource bounds in the half-trace process metric](inefficient_record.md).

## Reduction to preparing the mixed meters

For one slot, write $`p=p_N`$ and let

```math
\omega=(1-p)|00\rangle\langle00|+p|11\rangle\langle11|
 +\sqrt{\zeta p(1-p)}\bigl(|00\rangle\langle11|+|11\rangle\langle00|\bigr),
\qquad \Omega_N=\omega^{\otimes N}.
```

The [mixed-meter equivalence](inefficient_record.md#mixed-meter-and-resource-recovery) holds both ways. The chronological controlled-$`Z`$ circuit consumes $`\Omega_N`$ to implement the process. For any causal tester, its complete output is a channel of the supplied meter state, so purified distance from $`\Omega_N`$ upper-bounds the simulation error. Conversely, a tester sending fresh local $`|++\rangle`$ inputs, storing the quantum outputs, and making local sign-dependent corrections recovers $`\Omega_N`$ from the target process. Applying the same tester to an $`m`$-Bell simulator recovers a state $`\widetilde\Omega_N`$ within purified distance $`\varepsilon`$ and of Schmidt number at most $`2^m`$. The latter follows by conditioning on LOCC outcomes and discarding local systems. The tester uses local products and no shared entanglement.

## Upper bound from a pure meter and independent resets

Set $`r=(1-\zeta)p`$ and $`q=\zeta p/(1-r)`$. With $`|\phi_q\rangle=\sqrt{1-q}|00\rangle+\sqrt q|11\rangle`$, the following decomposition is exact:

```math
\omega=(1-r)|\phi_q\rangle\langle\phi_q|+r|11\rangle\langle11|.
```

The identity follows from $`(1-r)(1-q)=1-p`$ and $`(1-r)q=\zeta p`$. Shared randomness and local replacements therefore turn $`|\phi_q\rangle^{\otimes N}`$ into $`\Omega_N`$. The replacement independently discards each slot's two meter qubits and prepares $`|11\rangle`$ with probability $`r`$. It is a trace-preserving LOCC map, so it preserves the purified-error guarantee of any approximation to the pure input.

The squared Schmidt coefficient corresponding to each bit string of weight $`j`$ is $`q^j(1-q)^{N-j}`$. The total weight of shell $`j`$ is $`\Pr[Y_N=j]`$, with $`Y_N\sim\mathrm{Bin}(N,q)`$. Put $`u=\mu/N`$. The odds of $`q`$ obey

```math
\frac{q}{1-q}=\frac{\zeta p}{1-p}=\zeta\tanh u
\leq\zeta u\leq e^{\zeta u}-1.
```

It follows that $`q\leq 1-e^{-\zeta u}`$. For each slot, draw an independent $`\mathrm{Pois}(\zeta u)`$ variable and keep its nonempty indicator with independent probability $`q/(1-e^{-\zeta u})`$. The resulting indicators are independent Bernoulli variables with parameter $`q`$. Their sum is at most the sum of the Poisson variables, which has law $`X`$. Thus $`\Pr[Y_N\gt k]\leq\Pr[X\gt k]\leq\varepsilon^2`$ for every $`N`$, including equality in the defining Poisson inequality. Retaining all strings through weight $`k`$ captures at least $`1-\varepsilon^2`$ of the mass, using $`R=\sum_{j=0}^{\min(k,N)}\binom Nj=O_k(N^k)`$ strings.

The normalized Schmidt truncation has squared fidelity at least $`1-\varepsilon^2`$ with $`|\phi_q\rangle^{\otimes N}`$. Any pure state of Schmidt rank at most $`R`$ can be prepared from $`\lceil\log_2R\rceil`$ Bell pairs by LOCC, for example by preparing it locally and teleporting the compressed share. Applying the independent replacements and then the meter circuit proves the upper bound. For $`k=0`$, the truncation is the single vacuum string, so the entire construction starts with zero Bell pairs at every $`N`$.

## Lower bound from excitation subspaces

Assume $`k\geq1`$. For a weight $`w`$, use the orthonormal basis $`|S,S\rangle`$, with $`S\subseteq\{1,\ldots,N\}`$ and $`|S|=w`$. These are the maximally correlated bit strings with weight $`w`$ in both laboratories. The trace of the weight-$`w`$ block of $`\Omega_N`$ is $`\Pr[B_N=w]`$ with $`B_N\sim\mathrm{Bin}(N,p)`$. After dividing by this trace, the block entry at $`S,T`$ is

```math
\frac{\zeta^{w-|S\cap T|}}{\binom Nw}.
```

Each position at which the strings differ contributes one off-diagonal meter coefficient. There are $`2(w-|S\cap T|)`$ such positions.

For $`0\leq j\leq w`$, let $`W_j(S,J)=\mathbf 1_{J\subseteq S}`$, with columns indexed by $`j`$-element subsets $`J`$. The normalized block has the positive decomposition

```math
\frac{1}{\binom Nw}\sum_{j=0}^w
 \zeta^{w-j}(1-\zeta)^j W_jW_j^{\mathsf T}.
```

Indeed, the $`S,T`$ entry of $`W_jW_j^{\mathsf T}`$ is $`\binom{|S\cap T|}{j}`$. The binomial theorem gives the block entry above. Also, $`\mathrm{Tr}(W_jW_j^{\mathsf T})=\binom Nw\binom wj`$, so the traces of the summands are the probabilities of a binomial variable with parameters $`w,1-\zeta`$.

For $`k\leq w\leq N`$, let $`P_w`$ project onto the embedded column space of $`W_{w-k}`$. Its range contains the column space of every $`W_j`$ with $`j\leq w-k`$. To see this for $`j\leq t=w-k`$, sum the columns of $`W_t`$ over all $`t`$-sets containing a fixed $`j`$-set $`J`$. The result is $`\binom{w-j}{t-j}W_j(\cdot,J)`$. The probability detected by $`P_w`$ in the normalized block is consequently at least $`\Pr[\mathrm{Bin}(w,\zeta)\geq k]`$.

For a fixed integer $`W\geq k`$, set $`P_* = \sum_{w=k}^W P_w`$ for $`N\geq W`$. The ranges at different weights are orthogonal, so $`P_*`$ is a projector. It serves as a mathematical fidelity witness on the state recovered by the LOCC tester. Its target probability satisfies

```math
a_N=\mathrm{Tr}(P_*\Omega_N)
\geq \sum_{w=k}^{W}\Pr[B_N=w]\Pr[\mathrm{Bin}(w,\zeta)\geq k].
```

For fixed $`W`$ the sum converges to the same expression with $`B\sim\mathrm{Pois}(\mu)`$ in place of $`B_N`$. As $`W`$ increases, the limiting sum tends to $`\Pr[X\geq k]`$ by Poisson thinning. Minimality of $`k`$ gives $`\Pr[X\geq k]\gt \varepsilon^2`$. Choose a finite $`W`$ for which the truncated limit is already strictly above $`\varepsilon^2`$. Then $`a_N\geq\varepsilon^2+\delta`$ for some $`\delta\gt 0`$ and all sufficiently large $`N`$.

The permutation symmetry of the column space makes all diagonal entries of $`P_w`$ on the weight-$`w`$ maximally correlated basis equal. The rank is at most the number of columns, $`\binom N{w-k}`$. Each such diagonal is therefore at most $`\binom N{w-k}/\binom Nw=O_{W,k}(N^{-k})`$, uniformly over $`k\leq w\leq W`$. For any normalized vector in the range of $`P_*`$, the squared magnitude of each basis coefficient is bounded by the corresponding diagonal entry of $`P_*`$. This follows by projecting the basis vector and applying Cauchy–Schwarz. The vector is maximally correlated, so these squared magnitudes are precisely its squared Schmidt coefficients.

For any unit vector of Schmidt rank at most $`R`$, its squared overlap with each unit vector in the range is at most the sum of the latter vector's largest $`R`$ squared Schmidt coefficients, hence at most $`c_{W,k}RN^{-k}`$. Taking the supremum over unit vectors in the range bounds its squared projection onto that range. By linearity the same bound holds for $`\mathrm{Tr}(P_*\sigma)`$ on every state $`\sigma`$ of Schmidt number at most $`R`$.

Measure $`\{P_*,I-P_*\}`$ on the target and the recovered simulator state, and write $`b_N=\mathrm{Tr}(P_*\widetilde\Omega_N)`$. By purified-distance contraction, their binary root fidelity is at least $`\sqrt{1-\varepsilon^2}`$. Since $`a_N\gt \varepsilon^2`$, the binary fidelity inequality gives

```math
b_N\geq
\bigl(\sqrt{a_N(1-\varepsilon^2)}-\varepsilon\sqrt{1-a_N}\bigr)^2.
```

For example, parameterize the two probability vectors as $`(\sin^2\alpha,\cos^2\alpha)`$ and $`(\sin^2\beta,\cos^2\beta)`$ with angles in $`[0,\pi/2]`$. Their purified distance is $`\sin|\alpha-\beta|`$, which yields the bound. The strict margin $`a_N\geq\varepsilon^2+\delta`$ makes the right-hand side uniformly positive. Since $`\widetilde\Omega_N`$ has Schmidt number at most $`2^m`$, it follows that $`2^m\geq cN^k`$ for some constant $`c\gt 0`$. This gives the lower bound $`m\geq k\log_2N-O_{\mu,\zeta,\varepsilon}(1)`$. For $`k=0`$, nonnegativity of the Bell supply suffices.

## Efficiency and error thresholds

The mean $`\zeta\mu`$ arises from the weaker pure meter in the construction and from thinning the excitation count in the converse. For example, at $`\mu=1`$ and $`\varepsilon=0.1`$, the coefficient is $`4`$ at $`\zeta=1`$, $`2`$ at $`\zeta=1/4`$, and $`1`$ at $`\zeta=1/10`$. For $`\zeta\leq-\ln(0.99)`$ in this example, the zero-Bell construction meets the error target at every $`N`$.
