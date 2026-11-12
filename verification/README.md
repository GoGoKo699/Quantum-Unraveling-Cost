# Finite verification

From the repository root, install `requirements.txt` if needed and run:

```bash
python tools/verify.py
```

This runs the deterministic tests, writes `verification/results.json`, and
regenerates `verification/resource_cost.svg`. The random seed is fixed. Tests
also run through `python -m unittest discover -s tests -v`.

The checks reconstruct the local meter from its two controlled-Z gates and
actual X measurements, compare the complete branch maps through Choi matrices,
and use arbitrary mixed data with a reference. They check equality of the unread
diffusive channel and the random product-Pauli jump channel; seize multiple
meters, including a complex meter correlated across time; and apply a joint
resource approximation to a two-slot, record-dependent tester with local reference
couplings. The last example checks purified-distance contraction for that tester.
It does not enumerate all possible adaptive testers.

For small blocks the suite independently enumerates and sorts all Schmidt
probabilities, then compares the minimal rank and captured mass with the grouped
shell implementation. Exact integer arithmetic handles partial shells, exact
ties, tiny rational perturbations, and zero error. The rank routine interprets
the supplied finite-decimal or rational `p` and `epsilon` exactly. It first puts
every probability over a common denominator and uses integer comparisons and
ceilings. It does not compute a floating-point ceiling of an almost integral
ratio. At zero error and nonzero entanglement it returns rank `2**N` directly.

The physical value `p_N=(1-exp(-2 mu/N))/2` is transcendental in general.
`p_step` evaluates it using 60 decimal digits for the reported table. Thus those
rank calculations are exact for the displayed rational approximation to `p_N`,
not symbolic or interval-certified decisions at arbitrary transcendental
equality points. Tests at Poisson boundaries use 70-digit evaluations with a
finite positive margin; the coupling argument in the scientific account, not a
rounded numerical CDF, settles the analytical equality case. Very large exact
finite calculations can require large integers; this verifier makes no efficient
symbolic-computation claim.

Further checks cover finite binomial/Poisson CDF ordering, a limiting-CDF equality
case, the zero-supply regime, a nonboundary fourth-shell example, exact Bell-pair
rank cost, and the asymptotic growth of exact pure-resource entropy. The plot
keeps exact entropy ebits, approximate whole Bell pairs, and zero-error Bell
pairs distinct. They are different resource conventions.

The mixed-meter extension is checked by spectrally injecting the physical
two-qubit mixed state into the controlled-Z/X-readout circuit. Its complete
branch Choi maps and backaction on referenced inputs are compared with the
stated inefficient instrument. For two through four time slots and
`zeta=0,0.2,1`, a separately assembled dense circuit checks resource seizing,
local X-weight-one projection probability, the normalized projected state,
and its maximally-entangled fidelity. These are finite matrix checks of the
robustness mechanism; they do not prove its asymptotic resource converse.

These checks can catch finite circuit, normalization, spectrum-ordering,
quantile, and resource-convention errors. They are not proofs of the causal
simulation theorem, the Schmidt-number converse, the coupling result, asymptotic
optimality, novelty, or physical implementability. Those arguments and their
scope belong in `science/` and the related-work comparison.
