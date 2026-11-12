# Two weak slots, one joint resource

This example uses two calls to the efficient parity instrument with $`p=0.1`$. Its purpose is to make the exact finite-error Bell cost visible before taking a large-$`N`$ limit. The definitions and source conventions are in the [Wilde bridge](WILDE_BRIDGE.md); the general theorem is in [Bell cost](../science/bell_cost.md).

## What the detector does

Alice and Bob hold one qubit each. Let $`Q=Z_A\otimes Z_B`$. The measurement strength is

```math
\eta=2\sqrt{p(1-p)}=0.6,
\qquad
M_s=\frac{\sqrt{0.9}\,I+s\sqrt{0.1}\,Q}{\sqrt2}.
```

The unread channel applies no kick with probability $`0.9`$ and the product kick $`Q`$ with probability $`0.1`$. Shared randomness and local $`Z`$ gates implement it without entanglement.

The recorded instrument does more. On a product input $`|++\rangle`$, either sign has probability $`1/2`$. After correcting the negative sign locally, the pair is

```math
|\phi\rangle
=\sqrt{0.9}|++\rangle+\sqrt{0.1}|--\rangle.
```

Remove and save that pair, insert a fresh $`|++\rangle`$, and repeat. The saved target is $`|\phi\rangle^{\otimes2}`$. The two slots can also act on arbitrary user inputs; the shared-meter circuit implements the same instrument in that case.

## Inspect its four Schmidt probabilities

For this table only, label $`|+\rangle`$ by $`0`$ and $`|-\rangle`$ by $`1`$. A string specifies the two local archived qubits. Alice and Bob carry the same string in every Schmidt term.

| Alice's string | Bob's string | Probability | Cumulative largest-first mass |
|---|---|---:|---:|
| 00 | 00 | 0.81 | 0.81 |
| 01 | 01 | 0.09 | 0.90 |
| 10 | 10 | 0.09 | 0.99 |
| 11 | 11 | 0.01 | 1.00 |

The equal middle terms can be ordered either way. Exact simulation requires all four nonzero terms, hence two Bell pairs. If arbitrary shared pure states are priced by their entropy instead, the exact minimum is $`2h_2(0.1)\approx0.938`$ ebits. That entropy value is not an exact supply of $`0.938`$ Bell pairs.

## Allow purified strategy error 0.2

The tolerance is for the whole two-slot experiment, uniformly over the user's allowed interventions. It uses purified distance $`P=\sqrt{1-F^2}`$, with root fidelity $`F`$.

The required retained Schmidt mass is

```math
1-\epsilon^2=1-0.2^2=0.96.
```

Two terms retain only $`0.90`$, which is insufficient. Three retain $`0.99`$, so

```math
R_{0.2}=3,\qquad
C_P^{0.2}(2,0.1)=\lceil\log_2 3\rceil=2.
```

The normalized three-term resource omits the $`11`$ term. Its squared overlap with the target is $`0.99`$, giving purified distance $`\sqrt{0.01}=0.1`$. The resource rank decreases from four to three, but the integer Bell count remains two.

The converse is also visible: one Bell pair has Schmidt rank two. Any LOCC simulator supplied with it has Schmidt number at most two on the separable fresh-probe test. Its overlap with this pure target cannot exceed $`0.90`$, so its purified error is at least $`\sqrt{0.10}\approx0.316`$. It cannot meet the requested $`0.2`$.

## A nearby tolerance shows the integer saving

At $`\epsilon=0.35`$, the required mass is $`0.8775`$. The largest two terms retain $`0.90`$, so rank two suffices and the exact cost is one Bell pair. At $`\epsilon=0.45`$, the first term alone meets the threshold, giving zero Bell cost.

| Whole-process tolerance | Required mass | Minimum rank | Bell pairs |
|---:|---:|---:|---:|
| 0 | 1 | 4 | 2 |
| 0.20 | 0.96 | 3 | 2 |
| 0.35 | 0.8775 | 2 | 1 |
| 0.45 | 0.7975 | 1 | 0 |

For example, the two-term resource at tolerance $`0.35`$ can omit the first slot's weak excitation and retain the second slot's resource. Keeping no excitations in either slot retains only $`0.81`$ and has purified error $`\sqrt{0.19}\approx0.436`$, so that product approximation fails at tolerance $`0.35`$.

## Why the error covers adaptive use

Prepare the selected truncated **joint** resource before the run. The two local meter interactions, their outcomes, and any user operations form a quantum channel of that initial resource. The purified distance cannot increase through this channel. Consequently the retained mass calculation controls the complete experiment, including outcome registers, reference systems and data removed between the two slots.

This is why one first compresses the joint resource and then executes the causal protocol. Assigning a separate arbitrary tolerance to each slot would answer a different accounting question and can miss the best collective approximation.

For a continuous-monitoring interpretation one chooses $`\mu=-\ln(0.8)`$ at $`N=2`$, so that $`p_N=(1-e^{-2\mu/N})/2=0.1`$. As $`N`$ increases while that $`\mu`$ stays fixed, the individual slot probabilities change. The [Poisson law](../science/poisson_limit.md) analyzes that family; this two-slot table is an exact finite example rather than evidence for its asymptotic proof.
