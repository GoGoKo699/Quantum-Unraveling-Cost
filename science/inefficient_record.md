# A noisy binary record retains the logarithmic resource cost

[Model](model.md) · [Efficient resource equivalence](resource_equivalence.md) · [Fixed-error Bell cost](bell_cost.md) · [Unraveling gap](unraveling_gap.md)

The logarithmic lower bound survives a specified detector imperfection: independently flipping each weak binary sign with fixed contrast. The resulting instrument has the same unread parity-dephasing channel and a weaker measurement signal. For every fixed positive efficiency, its initial Bell-pair supply is still of order $`\log N`$ at a sufficiently small fixed total process error.

This is a robustness theorem for the instrument defined below. It does not identify a sharp finite-error coefficient for inefficient monitoring, and it does not cover arbitrary detector noise or hardware imperfections.

## The instrument

Keep the model's parity observable $`Q=Z_A\otimes Z_B`$. For one slot write $`a=\sqrt{1-p}`$, $`b=\sqrt p`$, with $`0\lt p\lt 1/2`$. For $`0\leq\zeta\leq1`$, define

```math
\mathcal I_s^{(\zeta)}(\rho)
=\frac12\left[
(aI+s\sqrt\zeta\,bQ)\rho(aI+s\sqrt\zeta\,bQ)
+(1-\zeta)b^2Q\rho Q\right],
\qquad s\in\{+1,-1\}.
```

Equivalently,

```math
\mathcal I_s^{(\zeta)}(\rho)
=\frac12\left[a^2\rho+b^2Q\rho Q
+s\sqrt\zeta\,ab(Q\rho+\rho Q)\right].
```

The first expression displays completely positive branches. Their sum is the same unread channel for all $`\zeta`$:

```math
\sum_s\mathcal I_s^{(\zeta)}(\rho)
=(1-p)\rho+pQ\rho Q.
```

Their effects are

```math
\mathcal I_s^{(\zeta)\,*}(I)
=\frac{I+s\sqrt\zeta\,\eta Q}{2},
\qquad \eta=2\sqrt{p(1-p)}.
```

There is a direct classical readout interpretation. Let $`\mathcal I_s^{(1)}`$ be the efficient instrument. Passing its sign through an independent binary symmetric channel with flip probability $`f=(1-\sqrt\zeta)/2`$ gives exactly

```math
\mathcal I_s^{(\zeta)}
=(1-f)\mathcal I_s^{(1)}+f\mathcal I_{-s}^{(1)}.
```

This changes the conditional quantum output as well as the reported statistics. For the semigroup choice $`p=p_N=(1-e^{-2\mu/N})/2`$, the weak measurement signal is reduced by $`\sqrt\zeta`$ while the unread dephasing rate remains fixed. The [continuum account](continuum_and_cadence.md) explains the associated detector-efficiency convention.

Let $`\mathsf C_{N,p}^{(\zeta)}`$ denote $`N`$ independent chronological uses of this specified instrument with the accessible ports, free operations, and charged initial Bell supply of [the model](model.md). Denote the corresponding minimum initial supply under uniform half-trace process error at most $`\varepsilon`$ by $`C_{T,\zeta}^{\varepsilon}(N,p)`$.

## Mixed meter and resource recovery

Define the maximally correlated two-qubit state

```math
\omega_{p,\zeta}
=(1-p)|00\rangle\langle00|+p|11\rangle\langle11|
+\sqrt{\zeta p(1-p)}
\left(|00\rangle\langle11|+|11\rangle\langle00|\right).
```

It is positive because it is obtained from $`\phi_p`$ by a local dephasing channel that multiplies off-diagonal matrix elements by $`\sqrt\zeta`$. The [controlled-$`Z`$ meter circuit](resource_equivalence.md#one-slot), followed by local $`X`$ measurements and reporting the product sign, implements exactly $`\mathcal I_s^{(\zeta)}`$ when supplied with this mixed meter. This follows by expanding the two diagonal resource terms and its two off-diagonal terms in that circuit.

The same fresh-input tester also recovers the mixed meter. Feed $`|++\rangle`$ into one slot. The sign has probability $`1/2`$, and its normalized quantum output, in the local $`X`$ basis, has diagonal entries $`1-p,p`$ and off-diagonal entries $`s\sqrt{\zeta p(1-p)}`$. For sign $`s=-1`$, Alice's $`X_A`$ correction reverses the latter sign. Local Hadamards then give exactly $`\omega_{p,\zeta}`$. After this correction, discarding the sign does not change the quantum output.

Using fresh local product inputs and retaining all outputs thus recovers

```math
\Omega_{N,p,\zeta}=\omega_{p,\zeta}^{\otimes N}.
```

This establishes an exact mixed-resource/process equivalence of the same kind as the efficient equivalence. It does not reduce the mixed-state Bell cost to the pure-state rank-tail formula. The converse below instead extracts a particular large-dimensional entangled sector.

## A finite-$`N`$ lower bound

Set

```math
q_N=Np(1-p)^{N-1},
\qquad
g_N=\zeta+\frac{1-\zeta}{N}.
```

For $`N\geq2`$ and $`0\leq\varepsilon\lt 1`$,

```math
\boxed{
C_{T,\zeta}^{\varepsilon}(N,p)
\geq(q_Ng_N-\varepsilon)\log_2N-1.
}
```

The right side may be negative; the nonnegative integer cost then gives the stronger trivial lower bound. The inequality charges a deterministic initial Bell supply and retains all success/failure probabilities.

### The one-excitation sector

At each laboratory project the recovered $`N`$ qubits onto the subspace of Hamming weight one. Write $`|i\rangle`$ for the string with its only excitation at position $`i`$. Since $`\Omega_{N,p,\zeta}`$ is maximally correlated in the computational basis, both local projections succeed together. Their joint success probability is $`q_N`$.

Every diagonal entry in the successful sector is $`p(1-p)^{N-1}`$. For distinct $`i,j`$, the off-diagonal entry $`|i,i\rangle\langle j,j|`$ contains two off-diagonal factors of the one-pair resource and $`N-2`$ diagonal factors, giving

```math
\bigl(\sqrt{\zeta p(1-p)}\bigr)^2(1-p)^{N-2}
=\zeta p(1-p)^{N-1}.
```

The normalized successful state is therefore exactly

```math
\tau_{N,\zeta}
=\zeta|\Phi_N\rangle\langle\Phi_N|
+\frac{1-\zeta}{N}\sum_{i=1}^N|i,i\rangle\langle i,i|,
\qquad
|\Phi_N\rangle=\frac1{\sqrt N}\sum_{i=1}^N|i,i\rangle.
```

Its overlap with the maximally entangled vector is

```math
\langle\Phi_N|\tau_{N,\zeta}|\Phi_N\rangle=g_N.
```

The power $`\zeta`$ here is important: the original meter coherence has factor $`\sqrt\zeta`$, and two different excitation positions require two such factors.

### Transferring the sector witness through a process error

Suppose an $`m`$-Bell simulator has $`d_T\leq\varepsilon`$. Apply the resource-recovering tester, including its local corrections, to obtain a state $`\widetilde\Omega`$ with

```math
\frac12\|\widetilde\Omega-\Omega_{N,p,\zeta}\|_1
\leq\varepsilon.
```

Let $`\Pi_1`$ denote the local Hamming-weight-one projector and set

```math
W=(\Pi_1\otimes\Pi_1)
  |\Phi_N\rangle\langle\Phi_N|
  (\Pi_1\otimes\Pi_1).
```

The vector is embedded in the corresponding successful subspace, so $`0\leq W\leq I`$. If the local projection succeeds on $`\widetilde\Omega`$ with probability $`q'`$ and gives conditional state $`\tau'`$, write $`g'=\langle\Phi_N|\tau'|\Phi_N\rangle`$. Then

```math
q'g'=\mathrm{Tr}(W\widetilde\Omega)
\geq\mathrm{Tr}(W\Omega_{N,p,\zeta})-\varepsilon
=q_Ng_N-\varepsilon.
```

This inequality treats the sector overlap as one unconditional effect. It requires neither dividing the global error by $`q_N`$ nor asserting a separate error guarantee after postselection. If $`q'=0`$, the displayed statement still applies with its left side zero.

### Entanglement required by the successful state

Let $`E_R`$ be relative entropy of entanglement, with logarithms in base two:

```math
E_R(\rho)=\inf_{\sigma\in\mathrm{SEP}}D(\rho\|\sigma).
```

For any state $`\rho`$ on $`\mathbb C^N\otimes\mathbb C^N`$ with $`g=\langle\Phi_N|\rho|\Phi_N\rangle`$,

```math
E_R(\rho)\geq g\log_2N-1.
```

For $`g\geq1/N`$, every separable state has overlap at most $`1/N`$ with $`\Phi_N`$. Applying the binary measurement $`\{\Phi_N,I-\Phi_N\}`$ and data processing for relative entropy gives

```math
E_R(\rho)
\geq D_{\mathrm{bin}}(g\|1/N)
\geq g\log_2N-h_2(g)
\geq g\log_2N-1.
```

When $`g\lt 1/N`$, the last right side is negative and follows instead from $`E_R\geq0`$.

The initial $`m`$ Bell pairs have $`E_R=m`$. LOCC monotonicity, including the selective local projection and its public success flag, yields $`m\geq q'E_R(\tau')`$. Therefore

```math
m\geq q'g'\log_2N-q'
\geq(q_Ng_N-\varepsilon)\log_2N-1,
```

as claimed. Failure branches are not discarded for free in this argument: their nonnegative entanglement terms have only been omitted from a lower bound on the full flagged ensemble.

## Uniform upper bound

Prepare an $`\varepsilon`$-approximation, in purified distance, to the efficient resource $`\Phi_{N,p}`$ using the [optimal Schmidt truncation](bell_cost.md#achievability). Apply a local dephasing channel to Alice's half of each meter with coherence factor $`\sqrt\zeta`$. On the ideal resource this gives $`\Omega_{N,p,\zeta}`$. Contractivity keeps the replacement resource within purified distance $`\varepsilon`$ of the mixed target resource.

Run the mixed-meter circuit chronologically. The same complete-experiment contractivity proves a uniform purified process error at most $`\varepsilon`$, and hence half-trace process error at most $`\varepsilon`$. Consequently,

```math
\boxed{
C_{T,\zeta}^{\varepsilon}(N,p)
\leq C_P^{\varepsilon}(N,p).
}
```

The right side is the efficient instrument's exact rank-tail cost. It is an upper bound here, not a claimed optimum for the mixed resource.

## Fixed-time consequence

Take $`p=p_N=(1-e^{-2\mu/N})/2`$ with fixed $`\mu>0`$ and fixed $`0\lt \zeta\leq1`$. Then

```math
q_N\longrightarrow\mu e^{-\mu},
\qquad g_N\longrightarrow\zeta.
```

For any fixed error satisfying

```math
0\lt \varepsilon\lt \zeta\mu e^{-\mu},
```

the finite lower bound has a positive logarithmic coefficient for all sufficiently large $`N`$. The efficient upper bound is $`O_{\mu,\varepsilon}(\log N)`$. Hence

```math
\boxed{
C_{T,\zeta}^{\varepsilon}(N,p_N)
=\Theta_{\mu,\zeta,\varepsilon}(\log N).
}
```

The same order holds under purified process error in this sufficient regime: a purified-error simulator also satisfies the trace-distance criterion used in the lower bound, and the upper is already a purified-error construction. No equality of their sharp coefficients is asserted.

At $`\zeta=0`$ the instrument instead factors as a fair reported sign and the unread LOCC channel:

```math
\mathcal I_s^{(0)}(\rho)
=\frac12\bigl[(1-p)\rho+pQ\rho Q\bigr].
```

Publicly sample the product-operation jump and an independent fair sign. This implements every slot exactly with zero entanglement, including under arbitrary interventions. Thus the logarithmic result requires fixed positive record contrast; it is not uniform as $`\zeta\to0`$.

## Attribution and limits

Mixed-entangled meters for individual nonlocal product measurements are established in [Jiang, Li and Li, Optics Express 31, 12508–12519 (2023)](https://doi.org/10.1364/OE.487883). The present lower bound concerns the complete chronological experiment at fixed global error, using its recoverable entangled sector. It does not claim the invention of mixed-meter nonlocal measurements. The relative-entropy monotonicity and overlap estimate used in the converse are standard entanglement tools; their application is displayed above rather than inferred from a numerical witness.

The detector model is independent binary sign corruption, equivalently the displayed dephased meter. The result does not cover record errors with arbitrary temporal correlations, inaccessible signs, general noisy local storage, limited local control, quantum communication, finite-speed feedback, or an efficiency that vanishes with $`N`$. The sufficient error threshold comes from one chosen excitation sector and is not claimed optimal. General exact or fixed-error Bell costs for the mixed meter are not determined here.

