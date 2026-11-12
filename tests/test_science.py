"""Finite checks with independent matrix/spectrum constructions."""
from decimal import Decimal, localcontext
from fractions import Fraction
import itertools
import math
import unittest

import numpy as np
from scipy.stats import binom, poisson

from tools.verify import (
    H, Q, adaptive_output_branches, binary_entropy, choi,
    cq_purified_distance, desired_kraus, exact_rank_tail,
    local_meter_kraus, maximally_correlated_resource, p_step,
    random_density, seize_resource, tensor_power,
)


def exhaustive_rank(n, p, epsilon):
    """Enumerate and sort every tensor-product Schmidt probability."""
    spectrum = []
    for bits in itertools.product((0, 1), repeat=n):
        value = Fraction(1)
        for bit in bits:
            value *= p if bit else 1 - p
        spectrum.append(value)
    spectrum.sort(reverse=True)
    target = 1 - epsilon * epsilon
    mass = Fraction(0)
    for i, value in enumerate(spectrum, 1):
        mass += value
        if mass >= target:
            return i, mass, spectrum
    raise AssertionError("full probability mass did not reach target")


class MeterCircuitTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(730101)

    def test_full_matrix_circuit_matches_instrument_choi(self):
        """Choi equality checks branch maps, not only POVM probabilities."""
        for p in [0.0, .001, .07, .2, .499999, .5]:
            raw = local_meter_kraus(p)
            completeness = sum(k.conj().T @ k for k in raw.values())
            np.testing.assert_allclose(completeness, np.eye(4), atol=3e-15)
            for s in (-1, 1):
                grouped = [k for (u, v), k in raw.items() if u * v == s]
                np.testing.assert_allclose(
                    choi(grouped), choi([desired_kraus(p, s)]), atol=3e-13)

    def test_arbitrary_mixed_inputs_with_reference(self):
        # Reference dimension three prevents a test restricted to pure |++> data.
        rho = random_density(12, self.rng)
        for p in [.005, .15, .42]:
            raw = local_meter_kraus(p)
            for s in (-1, 1):
                actual = np.zeros_like(rho)
                for (u, v), k in raw.items():
                    if u * v == s:
                        kr = np.kron(k, np.eye(3))
                        actual += kr @ rho @ kr.conj().T
                ideal = np.kron(desired_kraus(p, s), np.eye(3))
                np.testing.assert_allclose(actual, ideal @ rho @ ideal.conj().T,
                                           atol=3e-14)

    def test_unread_and_jump_channels_are_identical(self):
        rho = random_density(8, self.rng)
        qr = np.kron(Q, np.eye(2))
        for p in [0, .003, .15, .5]:
            raw = local_meter_kraus(p)
            unread = sum(np.kron(k, np.eye(2)) @ rho @ np.kron(k, np.eye(2)).conj().T
                         for k in raw.values())
            jump = (1 - p) * rho + p * qr @ rho @ qr
            np.testing.assert_allclose(unread, jump, atol=3e-14)

    def test_seizing_spectrum_and_multiple_slots(self):
        for n, p in [(1, .21), (2, .09), (3, .031)]:
            coefficients = np.array([
                math.sqrt(p ** z.bit_count() * (1 - p) ** (n - z.bit_count()))
                for z in range(1 << n)
            ], complex)
            err, prob_err = seize_resource(n, coefficients)
            self.assertLess(err, 3e-14)
            self.assertLess(prob_err, 3e-15)
            # Independently diagonalize the bipartite coefficient matrix.
            resource = maximally_correlated_resource(coefficients).reshape(1 << n, -1)
            singular = np.linalg.svd(resource, compute_uv=False) ** 2
            expected = sorted((abs(c) ** 2 for c in coefficients), reverse=True)
            np.testing.assert_allclose(singular, expected, atol=3e-15)

    def test_seizing_correlated_complex_joint_meter(self):
        # This meter is entangled across time slots, not a product of n meters.
        coefficients = self.rng.normal(size=8) + 1j * self.rng.normal(size=8)
        coefficients /= np.linalg.norm(coefficients)
        err, prob_err = seize_resource(3, coefficients)
        self.assertLess(err, 3e-14)
        self.assertLess(prob_err, 3e-15)

    def test_joint_resource_contractivity_under_adaptive_tester(self):
        n, p = 2, .14
        coefficients = np.array([
            math.sqrt(p ** z.bit_count() * (1 - p) ** (n - z.bit_count()))
            for z in range(1 << n)
        ])
        exact = maximally_correlated_resource(coefficients)
        # Retain just three leading Schmidt terms, normalize once globally.
        kept = coefficients.copy()
        kept[np.argmin(abs(kept))] = 0
        kept /= np.linalg.norm(kept)
        approximate = maximally_correlated_resource(kept)
        data = self.rng.normal(size=64) + 1j * self.rng.normal(size=64)
        data /= np.linalg.norm(data)
        a = adaptive_output_branches(exact, data)
        b = adaptive_output_branches(approximate, data)
        self.assertAlmostEqual(sum(np.vdot(x, x).real for x in a), 1, places=13)
        self.assertAlmostEqual(sum(np.vdot(x, x).real for x in b), 1, places=13)
        input_distance = math.sqrt(1 - abs(np.vdot(exact, approximate)) ** 2)
        self.assertLessEqual(cq_purified_distance(a, b), input_distance + 3e-13)


class RankTailTests(unittest.TestCase):
    def test_exact_rank_against_exhaustive_spectra(self):
        for n in range(1, 10):
            for p in [Fraction(0), Fraction(1, 25), Fraction(1, 5),
                      Fraction(2, 5), Fraction(1, 2), Fraction(4, 5), Fraction(1)]:
                for eps in [Fraction(0), Fraction(1, 10), Fraction(3, 10),
                            Fraction(3, 5), Fraction(9, 10), Fraction(1)]:
                    actual = exact_rank_tail(n, p, eps)
                    rank, mass, spectrum = exhaustive_rank(n, p, eps)
                    self.assertEqual(actual.rank, rank, (n, p, eps))
                    self.assertEqual(actual.captured_mass, mass)
                    self.assertGreaterEqual(actual.captured_mass, 1 - eps * eps)
                    if actual.rank > 1:
                        self.assertLess(sum(spectrum[:actual.rank - 1]), 1 - eps * eps)

    def test_ties_and_tiny_perturbations_are_exact(self):
        # Vacuum probability (4/5)^2 = 16/25 = 1-(3/5)^2 exactly.
        self.assertEqual(exact_rank_tail(2, "0.2", "0.6").rank, 1)
        self.assertEqual(exact_rank_tail(2, "0.2", "0.599999999999999999999999999999").rank, 2)
        self.assertEqual(exact_rank_tail(2, "0.2", "0.600000000000000000000000000001").rank, 1)
        self.assertEqual(exact_rank_tail(1, "0.04", "0.2").rank, 1)
        # Uniform spectrum creates exact ties across every Hamming shell.
        self.assertEqual(exact_rank_tail(200, "0.5", "0.5").rank, 3 * (1 << 198))
        self.assertEqual(exact_rank_tail(200, "0.5", "0.5").bell_pairs, 200)

    def test_zero_error_rank_and_entropy_conventions(self):
        for n in [1, 4, 1000, 100000]:
            result = exact_rank_tail(n, "0.001", "0")
            self.assertEqual(result.rank, 1 << n)
            self.assertEqual(result.bell_pairs, n)
        self.assertEqual(exact_rank_tail(12, 0, 0).bell_pairs, 0)
        self.assertEqual(exact_rank_tail(12, 1, 0).bell_pairs, 0)
        for n in [100, 1000, 10000]:
            p = float(p_step(n, "1"))
            ent = n * binary_entropy(p)
            # Derived expansion at mu=1: log2 N + log2 e + o(1).
            self.assertLess(abs(ent - math.log2(n) - math.log2(math.e)), .09)
            self.assertLess(ent, n)

    def test_partial_terminal_shell_is_minimal(self):
        n, p, eps = 7, Fraction(1, 7), Fraction(2, 5)
        result = exact_rank_tail(n, p, eps)
        rank, mass, spectrum = exhaustive_rank(n, p, eps)
        self.assertEqual(result.rank, rank)
        self.assertEqual(result.captured_mass, mass)
        self.assertLess(result.used_in_shell, math.comb(n, result.cutoff_shell))
        last_weight = spectrum[result.rank - 1]
        self.assertLess(mass - last_weight, 1 - eps * eps)

    def test_numerical_poisson_coupling_order_including_boundaries(self):
        for mu in [.2, 1.0, 2.7]:
            for n in [5, 20, 100, 1000]:
                p = float(p_step(n, str(mu)))
                for k in range(8):
                    self.assertGreaterEqual(binom.cdf(k, n, p) + 3e-14,
                                            poisson.cdf(k, mu))
        # At equality target=PoissonCDF(1), finite cutoff is already <=1;
        # for large N it is exactly 1. This checks, rather than assumes,
        # which side of the boundary the finite process approaches from.
        with localcontext() as ctx:
            ctx.prec = 70
            mu = Decimal(1)
            target = (-mu).exp() * (1 + mu)
            eps = (1 - target).sqrt()
            for n in [20, 100, 1000]:
                result = exact_rank_tail(n, p_step(n, "1", 70), eps)
                self.assertEqual(result.cutoff_shell, 1)

    def test_zero_supply_regime(self):
        # target=.51 < exp(-.5), so the vacuum works for every finite N.
        for n in [1, 2, 10, 100, 1000]:
            result = exact_rank_tail(n, p_step(n, ".5"), ".7")
            self.assertEqual(result.rank, 1)
            self.assertEqual(result.bell_pairs, 0)
        # Check exact limiting-boundary target=exp(-mu), at high precision.
        with localcontext() as ctx:
            ctx.prec = 70
            eps = (1 - (-Decimal(".5")).exp()).sqrt()
            for n in [10, 100, 1000]:
                self.assertEqual(exact_rank_tail(n, p_step(n, ".5", 70), eps).rank, 1)

    def test_nonboundary_poisson_rank_growth(self):
        mu, eps = 1, Fraction(1, 10)
        cutoff = int(poisson.ppf(float(1 - eps * eps), mu))
        self.assertEqual(cutoff, 4)
        residuals = []
        for n in [512, 1024, 2048, 4096]:
            result = exact_rank_tail(n, p_step(n), eps)
            self.assertEqual(result.cutoff_shell, cutoff)
            residuals.append(math.log2(result.rank) - cutoff * math.log2(n))
        # Finite approach to a nonzero partial shell coefficient, not a fitted proof.
        self.assertLess(max(residuals) - min(residuals), .3)


def mixed_meter_state(p, zeta):
    omega = np.zeros((4, 4), complex)
    omega[0, 0], omega[3, 3] = 1 - p, p
    omega[0, 3] = omega[3, 0] = math.sqrt(zeta * p * (1 - p))
    return omega


def mixed_meter_circuit_kraus(p, zeta):
    """Spectral injection of the physical mixed meter into the full CZ circuit."""
    eigenvalues, vectors = np.linalg.eigh(mixed_meter_state(p, zeta))
    phases = [(-1) ** (da * ma + db * mb)
              for da, db, ma, mb in np.ndindex(2, 2, 2, 2)]
    controlled = np.diag(phases)
    result = {(u, v): [] for u in (-1, 1) for v in (-1, 1)}
    for value, vector in zip(eigenvalues, vectors.T):
        if value <= 1e-14:
            continue
        injection = np.kron(np.eye(4), vector[:, None]) * math.sqrt(value)
        for u, v in result:
            bra = np.kron(np.array([1, u]), np.array([1, v])) / 2
            result[u, v].append(np.kron(np.eye(4), bra[None, :])
                                @ controlled @ injection)
    return result


def reorder_slot_meters_to_parties(rho, n):
    # Slot order A0,B0,A1,B1,... becomes A0,A1,...,B0,B1,... .
    order = list(range(0, 2 * n, 2)) + list(range(1, 2 * n, 2))
    axes = order + [i + 2 * n for i in order]
    return rho.reshape((2,) * (4 * n)).transpose(axes).reshape(1 << (2 * n), -1)


def fresh_probe_mixed_archive(rho_meter, n, signs):
    """Dense data/meter amplitude map assembled from CZ phases and X bras.

    This uses no formula for the postselected weight-one state. The matrix maps
    an arbitrary mixed joint meter to one raw measurement branch on fresh plus
    probes, followed by the record-dependent local correction.
    """
    d = 1 << n
    phase_map = np.empty((d * d, d * d), complex)
    for data in range(d * d):
        da, db = divmod(data, d)
        for meter in range(d * d):
            ma, mb = divmod(meter, d)
            exponent = (da & ma).bit_count() + (db & mb).bit_count()
            sign = 1
            for i in range(2 * n):
                if meter & (1 << (2 * n - 1 - i)):
                    sign *= signs[i]
            phase_map[data, meter] = sign * (-1) ** exponent / (d * d)
    correction = sum((1 << (n - 1 - i)) for i in range(n)
                     if signs[i] * signs[n + i] == -1)
    phase_map = phase_map[np.arange(d * d) ^ (correction << n)]
    out = phase_map @ rho_meter @ phase_map.conj().T
    probability = np.trace(out).real
    return out / probability, probability


class MixedMeterTests(unittest.TestCase):
    def test_mixed_branch_maps_with_reference(self):
        rng = np.random.default_rng(4702026)
        rho = random_density(12, rng)
        for p in [.013, .16, .42]:
            for zeta in [0.0, .2, 1.0]:
                physical = mixed_meter_circuit_kraus(p, zeta)
                self.assertGreaterEqual(np.linalg.eigvalsh(mixed_meter_state(p, zeta)).min(),
                                        -2e-15)
                for s in (-1, 1):
                    actual = np.zeros_like(rho)
                    actual_kraus = []
                    for (u, v), kraus in physical.items():
                        if u * v == s:
                            actual_kraus.extend(kraus)
                            for k in kraus:
                                kr = np.kron(k, np.eye(3))
                                actual += kr @ rho @ kr.conj().T
                    a, b = math.sqrt(1 - p), math.sqrt(p)
                    k1 = (a * np.eye(4) + s * math.sqrt(zeta) * b * Q) / math.sqrt(2)
                    k2 = math.sqrt((1 - zeta) * p / 2) * Q
                    ideal = sum(np.kron(k, np.eye(3)) @ rho @ np.kron(k, np.eye(3)).conj().T
                                for k in [k1, k2])
                    np.testing.assert_allclose(actual, ideal, atol=3e-14)
                    np.testing.assert_allclose(choi(actual_kraus), choi([k1, k2]), atol=3e-14)

    def test_mixed_meter_seizing_and_weight_one_projection(self):
        p = .083
        for n in [2, 3, 4]:
            d = 1 << n
            basis_change = tensor_power(H, 2 * n)
            indices = [(1 << i) * (d + 1) for i in range(n)]
            for zeta in [0.0, .2, 1.0]:
                omega = mixed_meter_state(p, zeta)
                product = np.array([[1.0]], complex)
                for _ in range(n):
                    product = np.kron(product, omega)
                product = reorder_slot_meters_to_parties(product, n)
                expected_archive = basis_change @ product @ basis_change
                for signs in [[1] * (2 * n), [(-1) ** (i // 2) for i in range(2 * n)]]:
                    archived, raw_probability = fresh_probe_mixed_archive(product, n, signs)
                    self.assertAlmostEqual(raw_probability, 4.0 ** (-n), places=14)
                    np.testing.assert_allclose(archived, expected_archive, atol=3e-14)
                    # Actual local X-weight-one projections, implemented by
                    # changing basis and selecting matching one-hot indices.
                    x_coordinates = basis_change @ archived @ basis_change
                    selected = x_coordinates[np.ix_(indices, indices)]
                    q = np.trace(selected).real
                    self.assertAlmostEqual(q, n * p * (1 - p) ** (n - 1), places=13)
                    tau = selected / q
                    expected_tau = zeta * np.ones((n, n)) / n + (1 - zeta) * np.eye(n) / n
                    np.testing.assert_allclose(tau, expected_tau, atol=3e-14)
                    phi = np.ones(n) / math.sqrt(n)
                    fidelity = np.vdot(phi, tau @ phi).real
                    self.assertAlmostEqual(fidelity, zeta + (1 - zeta) / n, places=13)


if __name__ == "__main__":
    unittest.main()
