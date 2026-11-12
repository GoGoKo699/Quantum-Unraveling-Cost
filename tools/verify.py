#!/usr/bin/env python3
"""Deterministic finite checks for distributed diffusive parity monitoring.

Run from the repository root: python tools/verify.py
Exact rank calculations are integer arithmetic for the *supplied rational*
parameters; p_N is evaluated to a stated Decimal precision before conversion.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
import json
import math
from pathlib import Path
import platform
import sys
import unittest

import numpy as np
import scipy
from scipy.stats import binom, poisson

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
Q = np.diag([1, -1, -1, 1]).astype(complex)


def rational(value: Fraction | Decimal | str | int | float) -> Fraction:
    """Read decimal notation exactly; floats use their displayed decimal value."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("parameter must be finite")
        return Fraction(str(value))
    return Fraction(value)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


@dataclass(frozen=True)
class RankTail:
    rank: int
    cutoff_shell: int
    used_in_shell: int
    captured_mass: Fraction

    @property
    def bell_pairs(self) -> int:
        # Exact even at enormous integer ranks and powers of two.
        return (self.rank - 1).bit_length()


def exact_rank_tail(n: int, p, epsilon) -> RankTail:
    """Smallest positive Schmidt rank capturing at least 1-epsilon**2.

    Input p and epsilon are interpreted as exact rationals. No floating-point
    ceiling or cumulative-probability comparison is used. Shells have a common
    denominator b**n for p=a/b. This can require large integers at large n or
    long input decimals: it is a correctness-oriented finite verifier, not a
    claimed efficient symbolic algorithm for transcendental p_N.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    p, epsilon = rational(p), rational(epsilon)
    if not 0 <= p <= 1 or not 0 <= epsilon <= 1:
        raise ValueError("p and epsilon must lie in [0,1]")
    p = min(p, 1 - p)  # Same Schmidt spectrum, decreasing shells now k=0,...,n.
    if p == 0:
        return RankTail(1, 0, 1, Fraction(1))
    if epsilon == 0:
        # Every Schmidt term is nonzero; avoid a numerically ill-conditioned tail.
        return RankTail(1 << n, n, 1, Fraction(1))
    threshold = 1 - epsilon * epsilon
    if threshold == 0:
        return RankTail(1, 0, 1, (1 - p) ** n)
    a, b = p.numerator, p.denominator
    c = b - a
    denominator = pow(b, n)
    # Captured probability is an integer numerator / denominator.
    needed = ceil_div(threshold.numerator * denominator, threshold.denominator)
    weight = pow(c, n)
    cumulative = 0
    rank = 0
    for k in range(n + 1):
        multiplicity = math.comb(n, k)
        shell = multiplicity * weight
        if cumulative + shell >= needed:
            used = ceil_div(needed - cumulative, weight)
            # Strictly positive since the preceding shell did not meet threshold.
            assert 1 <= used <= multiplicity
            captured = Fraction(cumulative + used * weight, denominator)
            return RankTail(rank + used, k, used, captured)
        cumulative += shell
        rank += multiplicity
        # c divides weight while k<n; retain exact common-denominator arithmetic.
        if k < n:
            weight = (weight // c) * a
    raise AssertionError("a full spectrum must capture every threshold <=1")


def p_step(n: int, mu="1", digits: int = 60) -> Decimal:
    if n < 1 or rational(mu) < 0:
        raise ValueError("n>=1 and mu>=0 are required")
    with localcontext() as ctx:
        m = Decimal(str(mu))
        if m == 0:
            return Decimal(0)
        # Guard the subtraction 1-exp(-x) when x is much smaller than one.
        ctx.prec = digits + len(str(n)) + max(0, -m.adjusted()) + 8
        value = (1 - (-2 * m / n).exp()) / 2
        ctx.prec = digits
        return +value


def binary_entropy(p: float) -> float:
    if p in (0.0, 1.0):
        return 0.0
    return (-p * math.log(p) - (1 - p) * math.log1p(-p)) / math.log(2)


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = z @ z.conj().T
    return rho / np.trace(rho)


def local_meter_kraus(p: float) -> dict[tuple[int, int], np.ndarray]:
    """Assemble two actual controlled-Z gates, resource injection, and X bras.

    Qubit order: data A, data B, meter A, meter B. This assembly is deliberately
    independent of the closed form for the desired Lüders instrument.
    """
    resource = np.array([math.sqrt(1 - p), 0, 0, math.sqrt(p)], complex)
    injection = np.kron(np.eye(4), resource[:, None])
    phases = []
    for bits in np.ndindex(2, 2, 2, 2):
        da, db, ma, mb = bits
        phases.append((-1) ** (da * ma + db * mb))
    controlled = np.diag(phases)
    result = {}
    for u in (-1, 1):
        for v in (-1, 1):
            bra = np.kron(np.array([1, u]), np.array([1, v])) / 2
            readout = np.kron(np.eye(4), bra[None, :])
            result[u, v] = readout @ controlled @ injection
    return result


def desired_kraus(p: float, s: int) -> np.ndarray:
    # Spectral functional calculus of the POVM effects, not the meter circuit.
    # High precision avoids cancellation of 1-eta near a projective meter.
    with localcontext() as ctx:
        ctx.prec = 60
        pd = Decimal(str(p))
        eta = 2 * (pd * (1 - pd)).sqrt()
        entries = [float(((1 + s * int(q) * eta) / 2).sqrt())
                   for q in np.diag(Q).real]
    return np.diag(entries)


def choi(kraus: list[np.ndarray]) -> np.ndarray:
    return sum(np.outer(k.reshape(-1, order="F"),
                        k.reshape(-1, order="F").conj()) for k in kraus)


def apply_gate(psi: np.ndarray, gate: np.ndarray, axes: tuple[int, ...],
               n_qubits: int) -> np.ndarray:
    axes = tuple(axes)
    other = tuple(i for i in range(n_qubits) if i not in axes)
    perm = axes + other
    tensor = psi.reshape((2,) * n_qubits).transpose(perm)
    tensor = (gate @ tensor.reshape(1 << len(axes), -1)).reshape((2,) * n_qubits)
    return tensor.transpose(np.argsort(perm)).reshape(-1)


def tensor_power(a: np.ndarray, n: int) -> np.ndarray:
    out = np.array([1.0], complex)
    for _ in range(n):
        out = np.kron(out, a)
    return out


def maximally_correlated_resource(coefficients: np.ndarray) -> np.ndarray:
    """sum_z c_z |z>_A |z>_B, with the party registers contiguous."""
    d = len(coefficients)
    out = np.zeros(d * d, complex)
    out[np.arange(d) * (d + 1)] = coefficients
    return out


def seize_resource(n: int, coefficients: np.ndarray) -> tuple[float, float]:
    """Full tensor circuit on n fresh |++> probes, including correlated meters.

    Returns the largest corrected-state error and raw-outcome probability error.
    The coefficients can be complex and need not factor across time slots.
    """
    d = 1 << n
    resource = maximally_correlated_resource(coefficients)
    data = np.ones(d * d, complex) / d
    psi = np.kron(data, resource)
    nq = 4 * n
    cz = np.diag([1, 1, 1, -1])
    for i in range(n):
        psi = apply_gate(psi, cz, (i, 2 * n + i), nq)
        psi = apply_gate(psi, cz, (n + i, 3 * n + i), nq)
    # Rows data(A then B), columns meters(A then B).
    matrix = psi.reshape(d * d, d * d)
    h_party = tensor_power(H, n)
    target = np.kron(h_party, h_party) @ resource
    state_error = probability_error = 0.0
    for outcome in range(1 << (2 * n)):
        bits = [(outcome >> (2 * n - 1 - i)) & 1 for i in range(2 * n)]
        signs = [(-1) ** b for b in bits]
        bra = np.array([1.0], complex)
        for sign in signs:
            bra = np.kron(bra, np.array([1, sign]) / math.sqrt(2))
        out = matrix @ bra.conj()
        probability = float(np.vdot(out, out).real)
        probability_error = max(probability_error, abs(probability - 4.0 ** (-n)))
        for i in range(n):
            if signs[i] * signs[n + i] == -1:
                out = apply_gate(out, X, (i,), 2 * n)
        out /= math.sqrt(probability)
        state_error = max(state_error, float(np.linalg.norm(out - target)))
    return state_error, probability_error


def adaptive_output_branches(resource: np.ndarray, data_reference: np.ndarray
                             ) -> list[np.ndarray]:
    """Two-slot tester with reference and record-dependent local interventions.

    Qubits: data A0,A1,B0,B1; two reference qubits; meter A0,A1,B0,B1.
    All meter raw outcomes remain in the classical branch label. Measured meter
    states may be retained since their states are fixed by that branch label.
    """
    nq = 10
    cz = np.diag([1, 1, 1, -1])
    branches = [(np.kron(data_reference, resource), ())]
    phase = np.diag([1, 1j])
    for slot in range(2):
        new = []
        for psi, record in branches:
            psi = apply_gate(psi, cz, (slot, 6 + slot), nq)
            psi = apply_gate(psi, cz, (2 + slot, 8 + slot), nq)
            for u in (-1, 1):
                for v in (-1, 1):
                    xu = np.array([1, u]) / math.sqrt(2)
                    xv = np.array([1, v]) / math.sqrt(2)
                    out = apply_gate(psi, np.outer(xu, xu), (6 + slot,), nq)
                    out = apply_gate(out, np.outer(xv, xv), (8 + slot,), nq)
                    if slot == 0:
                        # Distinct local feedback for the two parity records,
                        # and local coupling to reference memories.
                        out = apply_gate(out, H if u * v == 1 else phase, (1,), nq)
                        out = apply_gate(out, phase if u == 1 else H, (3,), nq)
                        out = apply_gate(out, cz, (0, 4), nq)
                        out = apply_gate(out, cz, (2, 5), nq)
                    new.append((out, record + (u, v)))
        branches = new
    return [psi for psi, _ in branches]


def cq_purified_distance(a: list[np.ndarray], b: list[np.ndarray]) -> float:
    root_fidelity = sum(abs(np.vdot(x, y)) for x, y in zip(a, b))
    return math.sqrt(max(0.0, 1 - min(1.0, root_fidelity) ** 2))


def finite_table(mu="1", epsilon="0.1", ns=None) -> list[dict]:
    if ns is None:
        ns = [8, 16, 32, 64, 100, 128, 256, 512, 1000, 1024, 2048, 4096, 8192]
    rows = []
    for n in ns:
        p_dec = p_step(n, mu, digits=60)
        p = float(p_dec)
        result = exact_rank_tail(n, p_dec, epsilon)
        rows.append({
            "N": n, "p_N_decimal_60_digits": str(p_dec),
            "epsilon_purified": str(epsilon), "cutoff_shell": result.cutoff_shell,
            "rank": result.rank, "bell_pairs_approximate": result.bell_pairs,
            "entropy_exact_pure_resource_ebits": n * binary_entropy(p),
            "bell_pairs_zero_error": n,
            "captured_mass_float": float(result.captured_mass),
            "binomial_cutoff_CDF_float": float(binom.cdf(result.cutoff_shell, n, p)),
        })
    return rows


def make_chart(rows: list[dict], path: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans"})
    n = np.array([r["N"] for r in rows])
    fig, ax = plt.subplots(figsize=(8.4, 4.9), layout="constrained")
    ax.loglog(n, n, color="#7c8793", linestyle="--", label="Zero-error Bell pairs: N")
    ax.loglog(n, [r["bell_pairs_approximate"] for r in rows], "o-",
              color="#006b70", label="Bell pairs at purified error 0.1")
    ax.loglog(n, [r["entropy_exact_pure_resource_ebits"] for r in rows], "s-",
              color="#ba5728", label="Exact pure-resource entropy: N h₂(pₙ)")
    ax.set(xlabel="Temporal resolution N (fixed μ = γT = 1)",
           ylabel="Resource amount (different conventions)",
           title="The record's cost depends on error and resource convention")
    ax.grid(True, which="major", alpha=.18)
    ax.legend(frameon=False, loc="upper left", fontsize=9)
    fig.text(.01, -.015, "Finite evaluations; entropy ebits and whole Bell pairs are distinct resources.",
             fontsize=8, color="#444444")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("verification/results.json"))
    parser.add_argument("--chart", type=Path, default=Path("verification/resource_cost.svg"))
    parser.add_argument("--no-chart", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))
    tests = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if not result.wasSuccessful():
        return 1
    rows = finite_table()
    output = {
        "validation": "finite deterministic checks, not proof or priority certification",
        "python": platform.python_version(), "numpy": np.__version__,
        "scipy": scipy.__version__, "tests_run": result.testsRun,
        "mu": "1", "p_evaluation_decimal_precision": 60,
        "rank_arithmetic": "exact integers for supplied finite-decimal p_N and epsilon",
        "finite_cases": rows,
        "poisson_nonboundary_coefficient_mu1_epsilon_point1": int(poisson.ppf(.99, 1)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    if not args.no_chart:
        args.chart.parent.mkdir(parents=True, exist_ok=True)
        make_chart(rows, args.chart)
    print(f"Passed {result.testsRun} tests; wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
