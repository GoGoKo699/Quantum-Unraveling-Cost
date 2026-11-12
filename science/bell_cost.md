# The exact Bell-pair supply at a fixed process error

[Model and error conventions](model.md) · [Resource equivalence](resource_equivalence.md) · [Poisson limit](poisson_limit.md) · [Exact resource distinctions](exact_resources.md)

The number of Bell pairs needed to simulate the full monitored process at a fixed global error is determined by a finite, explicitly computable Schmidt-probability tail. The result permits correlated simulators and arbitrary causal inputs.

## Resource and error being optimized

The simulator begins with $`m`$ maximally entangled qubit pairs, separable auxiliary states, and free local operations and classical communication. Every preshared entangled auxiliary must be generated from this charged supply. This is an initial Bell-pair supply cost, rather than a net entanglement consumption after crediting returned resources.

Let $`C_P^{\varepsilon}(N,p)`$ be the least integer $`m\geq0`$ for which a simulator of $`\mathcal C_{N,p}`$ has

```math
d_P\!\left(\mathcal C_{N,p},\widetilde{\mathcal C}\right)
=\sup_{\mathcal T}
P\!\left(\mathcal T[\mathcal C_{N,p}],
          \mathcal T[\widetilde{\mathcal C}]\right)
\leq\varepsilon.
```

The testers and their normalized final outputs are as in [the model](model.md). Root fidelity is $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$, and purified distance is $`P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}`$. In particular, for a normalized pure target,

```math
P(\rho,|\psi\rangle\langle\psi|)^2
=1-\langle\psi|\rho|\psi\rangle.
```

All logarithms below have base two.

## The rank-tail formula

List the squared Schmidt coefficients of $`|\Phi_{N,p}\rangle=|\phi_p\rangle^{\otimes N}`$ in decreasing order:

```math
\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_{2^N}\geq0.
```

For $`0\leq\varepsilon<1`$, define

```math
R_{\varepsilon}(N,p)
=\min\left\{R\geq1:
       \sum_{j=1}^{R}\lambda_j\geq1-\varepsilon^2\right\}.
```

Then

```math
\boxed{
C_P^{\varepsilon}(N,p)
=\left\lceil\log_2 R_{\varepsilon}(N,p)\right\rceil.
}
```

If the resource unit is a maximally entangled state of any integer rank $`M`$, rather than an integer number of qubit Bell pairs, the minimum rank is exactly $`R_{\varepsilon}(N,p)`$. Its logarithmic size is $`\log_2 R_{\varepsilon}(N,p)`$ without the outer ceiling.

### Converse

A bipartite state has Schmidt number at most $`R`$ if it admits an ensemble decomposition into pure states of Schmidt rank at most $`R`$. Local operations cannot increase a pure state's Schmidt rank in an individual outcome branch. Therefore an LOCC protocol beginning with $`m`$ Bell pairs and separable auxiliaries can produce only states of Schmidt number at most $`2^m`$, including after arbitrary local memories and classical records have been discarded.

For any normalized pure target $`|\psi\rangle`$ with squared Schmidt coefficients $`\lambda_j`$, and any state $`\rho`$ of Schmidt number at most $`R`$,

```math
\langle\psi|\rho|\psi\rangle
\leq\sum_{j=1}^{R}\lambda_j.
```

To prove this first for a pure state $`|v\rangle`$ of Schmidt rank at most $`R`$, let $`\Pi`$ project onto its local support at Alice. The support dimension is at most $`R`$, and

```math
|\langle\psi|v\rangle|^2
\leq\| (\Pi\otimes I)|\psi\rangle\|^2
=\mathrm{Tr}(\Pi\psi_A)
\leq\sum_{j=1}^{R}\lambda_j.
```

The last inequality is the variational characterization of the largest eigenvalue sums. Averaging proves the claim for a mixed state of Schmidt number at most $`R`$. No choice of classical mixture can exceed this bound.

Apply the [resource-recovering tester](resource_equivalence.md#recovering-the-resource-from-the-process) to a proposed simulator. It produces a state $`\rho`$ of Schmidt number at most $`2^m`$ with

```math
\langle\Phi_{N,p}|\rho|\Phi_{N,p}\rangle
\geq1-\varepsilon^2.
```

The overlap bound forces $`2^m\geq R_{\varepsilon}(N,p)`$. This proves the lower bound for arbitrary correlated and adaptive simulators in the stated resource model.

### Achievability

Keep the $`R=R_{\varepsilon}(N,p)`$ largest terms of the Schmidt expansion and normalize:

```math
|\widehat\Phi_R\rangle
=\frac{1}{\sqrt{s_R}}
  \sum_{j=1}^{R}\sqrt{\lambda_j}\,|a_j\rangle|b_j\rangle,
\qquad s_R=\sum_{j=1}^{R}\lambda_j.
```

Its squared overlap with the target is $`s_R`$, so its purified distance from the target is at most $`\varepsilon`$. It has Schmidt rank at most $`R`$ and can be prepared deterministically by LOCC from $`\lceil\log_2R\rceil`$ Bell pairs. This is the pure-state majorization criterion: the uniform spectrum on $`2^m`$ entries is majorized by the target spectrum of rank at most $`2^m`$.

Use this truncated state as the joint resource in the chronological meter circuit. Contractivity of purified distance, applied to the full resource-to-output map for every tester, gives uniform process error at most $`\varepsilon`$. The resource is generally correlated across slots, which is allowed. It need not consist of independent approximate meters.

The converse and this construction meet exactly. The ingredients are standard pure-state entanglement conversion and the explicit [resource/process equivalence](resource_equivalence.md); the finite-error conclusion does not rely on an entropy-continuity estimate in a dimension growing with $`N`$.

## Evaluating the rank without enumerating bit strings

Assume $`0<p<1/2`$. A Schmidt string of Hamming weight $`k`$ has probability

```math
w_k=(1-p)^{N-k}p^k
```

and multiplicity $`\binom Nk`$. Since $`w_{k+1}/w_k=p/(1-p)<1`$, the descending order consists of complete shells of increasing Hamming weight, followed possibly by part of one shell.

Write $`a=1-\varepsilon^2`$ and let $`B\sim\mathrm{Bin}(N,p)`$. Set

```math
k_N=\min\{k:\Pr(B\leq k)\geq a\}.
```

With $`\Pr(B\leq-1)=0`$ and an empty sum interpreted as zero,

```math
\boxed{
R_{\varepsilon}(N,p)
=\sum_{j=0}^{k_N-1}\binom Nj
+\left\lceil
\frac{a-\Pr(B\leq k_N-1)}
     {(1-p)^{N-k_N}p^{k_N}}
\right\rceil.
}
```

The numerator is strictly positive by minimality of $`k_N`$, and the final ceiling is no larger than $`\binom N{k_N}`$. Keeping the entire last shell is a valid upper bound, but the partial-shell expression is the exact minimum rank.

For $`p=0`$ the state is a product and the cost is zero. For $`p=1/2`$ all $`2^N`$ squared Schmidt coefficients are equal, so $`R_{\varepsilon}=\lceil(1-\varepsilon^2)2^N\rceil`$. The physical semigroup discretization has $`0<p_N<1/2`$ for finite positive $`\gamma,T,N`$.

## A trace-distance process error

For comparison, define $`C_T^{\varepsilon}(N,p)`$ using

```math
d_T(\mathcal C,\mathcal D)
=\sup_{\mathcal T}\frac12
\|\mathcal T[\mathcal C]-\mathcal T[\mathcal D]\|_1.
```

For normalized states, the Fuchs–van de Graaf inequalities imply

```math
d_T\leq d_P\leq\sqrt{2d_T}.
```

Thus, for $`0\leq\varepsilon<1/2`$,

```math
C_P^{\sqrt{2\varepsilon}}(N,p)
\leq C_T^{\varepsilon}(N,p)
\leq C_P^{\varepsilon}(N,p).
```

The exact rank-tail identity above is claimed for purified process error. This comparison transfers the logarithmic growth to trace-distance error in the nontrivial fixed-error regime stated in [the Poisson limit](poisson_limit.md). It does not assert the same sharp leading coefficient for the two error conventions.

