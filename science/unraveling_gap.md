# One generator, different distributed costs

The two-qubit generator

```math
\mathcal L_\gamma(\rho)=\gamma(Q\rho Q-\rho),
\qquad Q=Z_A\otimes Z_B,
```

has an implementation using local Pauli operations and shared randomness. An efficient weak parity measurement with the same unread evolution can create entanglement, because its classical record specifies coherent backaction rather than a random local Pauli. This page proves that distinction and identifies the access condition under which a whole QND record can still be simulated at constant cost.

All entanglement costs below permit unlimited local operations and classical communication. They do not require instantaneous spacelike communication. The finite-slot instrument is the exact object; [continuum and cadence](continuum_and_cadence.md) explains its relation to continuous monitoring.

## Exact unread evolution

For a slot of duration $`h`$, set

```math
p_h=\frac{1-e^{-2\gamma h}}2,
\quad a_h=\sqrt{1-p_h},\quad b_h=\sqrt{p_h},
\quad \eta_h=2a_hb_h=\sqrt{1-e^{-4\gamma h}}.
```

The efficient binary measurement has Kraus operators

```math
M_s=\sqrt{\frac{I+s\eta_h Q}{2}}
=\frac{a_hI+s b_hQ}{\sqrt2},\qquad s\in\{+1,-1\}.
```

The square-root identity follows by squaring its positive right-hand side. Summing its two branches cancels the cross terms:

```math
\sum_s M_s\rho M_s^
\dagger=(1-p_h)\rho+p_hQ\rho Q
=e^{h\mathcal L_\gamma}(\rho).
```

For the last equality, split $`\rho`$ into parts even and odd under conjugation by $`Q`$. The even part is fixed; the odd part is multiplied by $`1-2p_h=e^{-2\gamma h}`$, exactly the semigroup solution.

**Zero-entanglement simulation.** Draw a shared Bernoulli variable with probability $`p_h`$. On value one, Alice and Bob each apply their local $`Z`$; otherwise both apply the identity. This implements the channel above exactly. Draw independent variables in successive slots. Each slot is the correct channel on the data together with every reference, so composition with any intervening local instruments, feedback, or swaps remains exact. No entangled resource is needed.

This statement concerns the unread channel. A simulator that outputs the Bernoulli draw supplies a different instrument from the efficient binary measurement.

## The recorded jump unraveling is also free

A Poisson process of rate $`\gamma`$ implements the same semigroup. Each jump applies $`Q`$, which is a product unitary. Alice and Bob can share the Poisson record and apply their local $`Z`$ at its jump times. The probability of an odd number of jumps in a duration $`h`$ is $`p_h`$, so forgetting the record gives the preceding channel.

The jump record is state independent: $`Q^\dagger Q=I`$ makes the jump intensity constant. It contains the times of random local Pauli kicks, rather than information about the parity expectation. Under the declared free classical coordination, this recorded jump process costs zero entanglement, including in the presence of local interventions. This is an algebraic observation about this product-Pauli generator, not a statement that arbitrary quantum-jump records are free.

## The efficient binary record can create entanglement

Apply one measurement to the product input $`|+\rangle_A|+\rangle_B`$. Since $`Q|++\rangle=|--\rangle`$, either outcome occurs with probability $`1/2`$ and the normalized output is

```math
|\phi_s\rangle=a_h|++\rangle+s b_h|--\rangle.
```

The outcome-dependent local correction $`X_A`$ on the negative branch changes its relative sign and produces the same pure state in both branches:

```math
|\phi_{p_h}\rangle
=\sqrt{1-p_h}|++\rangle+\sqrt{p_h}|--\rangle.
```

For $`p_h>0`$ this state is entangled. Its entanglement entropy is $`h_2(p_h)`$, where $`h_2(p)=-p\log_2p-(1-p)\log_2(1-p)`$ is binary entropy. Thus exact simulation of the retained efficient instrument is not possible by LOCC alone. Fresh product probes inserted and archived at every slot produce a tensor product of these pure states. The resource lower bounds therefore concern the whole intervened record, rather than only its final data channel.

The matching shared-meter primitive is established prior work of [Vidil and Edamatsu](https://doi.org/10.1088/1367-2630/abee3f). In a locally rotated version, supply the meter $`a_h|00\rangle+b_h|11\rangle`$, apply a controlled-$`Z`$ locally from each meter half to its data qubit, and measure the two meter halves in the $`X`$ basis. Raw outcomes $`u,v\in\{\pm1\}`$ have Kraus operator

```math
K_{u,v}=\frac{a_h I+uv b_hQ}{2}.
```

Grouping the two raw branches with $`uv=s`$ gives $`M_s\rho M_s^\dagger`$. They are identical Kraus maps up to their common normalization, so grouping introduces no extra dephasing. The unused raw bit is uniformly random and independent of the input and the retained outcome. Each slot therefore consumes a meter with entropy $`h_2(p_h)`$ and implements the efficient instrument on arbitrary entangled inputs.

For $`N`$ equal slots over $`T`$, these two arguments match: the exact minimum initial pure-resource entropy is $`N h_2(p_{T/N})`$. Exact Bell-pair count is a separate quantity: each nonzero weak meter has Schmidt rank two, and the archived tensor state has rank $`2^N`$, giving an exact count of $`N`$ Bell pairs. Fixed whole-process approximation permits collective resource compression; it must not be priced by independently rounding each weak meter to one Bell pair.

## A whole QND record with no intermediate data access

There is a different, restricted interface in which the input data are supplied at time zero, all classical outcomes can be streamed, and the data are returned only after the last slot. No operation can act on the data at an intermediate slot boundary. In that interface, one Bell pair suffices for the full record and final conditional state, for every $`N`$ and every input, including inputs entangled with a reference.

Let $`\Pi_0=(I+Q)/2`$ and $`\Pi_1=(I-Q)/2`$. First implement the parity-tagging isometry

```math
V|\psi\rangle
=\Pi_0|\psi\rangle|0\rangle_b
+\Pi_1|\psi\rangle|1\rangle_b,
```

with $`b`$ held by Bob. Its construction consumes one Bell pair $`(|00\rangle_{ab}+|11\rangle_{ab})/\sqrt2`$: Alice applies CNOT from her data to $`a`$, measures $`a`$ in the computational basis, and sends the result $`m`$. Bob applies $`X_b^m`$. This coherently copies Alice's computational bit into $`b`$, with a uniformly random and input-independent message. Bob then applies CNOT from his data qubit to $`b`$, so $`b`$ stores their parity. Linear extension verifies this construction for arbitrary input-reference states.

In each slot Bob measures $`b`$ with

```math
L_s=\sqrt{\frac{I+s\eta_h Z_b}{2}}.
```

The identity $`(I\otimes L_s)V=VM_s`$ shows that a record $`\boldsymbol s`$ produces $`VK_{\boldsymbol s}`$, where $`K_{\boldsymbol s}=M_{s_N}\cdots M_{s_1}`$. Hence all record probabilities are correct. At the end Bob measures $`b`$ in the $`X`$ basis, obtaining $`t\in\{0,1\}`$. Its data Kraus operator is

```math
\langle (-)^t|_b VK_{\boldsymbol s}
=\frac{Q^t K_{\boldsymbol s}}{\sqrt2}.
```

Alice and Bob apply their local $`Z^t`$ corrections. Summing over the erased bit $`t`$ leaves exactly $`K_{\boldsymbol s}\rho K_{\boldsymbol s}^\dagger`$. Thus the record and final state coincide with the target instrument, with one Bell pair and no dependence on the number of slots. A simpler upper bound is two Bell pairs: teleport Alice's data to Bob, perform all measurements locally, and teleport it back.

The intermediate data marginal in the tagging protocol is already dephased between the two parity sectors. Final erasure restores the required conditional coherence. Therefore this construction does **not** supply the data at intermediate times with the correct accessible state. It cannot establish a constant cost for a tester that swaps out fresh data and archives each weakly entangled output. The difference in interface is exactly what the lower bound exploits.

## What the separation establishes

| Requested interface | Shared entanglement required |
|---|---|
| Unread product-Pauli evolution, with arbitrary local interventions | Zero |
| Recorded product-Pauli jumps, with arbitrary local interventions | Zero |
| Efficient binary parity record, input/final data only | At most one Bell pair |
| Efficient binary parity record with fresh-probe access at every slot | Grows with time resolution in the nontrivial fixed-error regime |

The last growth is a distributed implementation cost of the specified monitored process. A Lindblad generator fixes the unread dynamics but does not fix the unraveling, its recorded backaction, or the temporal interfaces offered to a user. Those additional choices affect the resource law.
