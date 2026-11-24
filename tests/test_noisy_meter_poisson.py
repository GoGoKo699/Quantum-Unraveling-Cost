"""Finite, independent checks for the noisy meter's purified-error law."""

from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest


def subsets(n, weight):
    return tuple(frozenset(items) for items in combinations(range(n), weight))


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def inclusion_basis(sets, patterns):
    """Construct an exact orthogonal basis for the selected incidence range."""
    basis = []
    for pattern in patterns:
        column = [Fraction(pattern <= row) for row in sets]
        for vector in basis:
            coefficient = dot(column, vector) / dot(vector, vector)
            column = [a - coefficient * b for a, b in zip(column, vector)]
        if any(column):
            basis.append(column)
    return basis


def projector_diagonal(basis, size):
    norms = [dot(vector, vector) for vector in basis]
    return [
        sum(vector[i] ** 2 / norm for vector, norm in zip(basis, norms))
        for i in range(size)
    ]


def binomial_cdf(n, p, cutoff):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j)
               for j in range(cutoff + 1))


def poisson_cdf(rate, cutoff):
    term = Decimal(1)
    total = term
    for j in range(1, cutoff + 1):
        term *= rate / j
        total += term
    return (-rate).exp() * total


class NoisyMeterPoissonTests(unittest.TestCase):
    def test_replacement_channel_preserves_target_populations_and_coherence(self):
        for p in [Fraction(0), Fraction(2, 9), Fraction(1, 2)]:
            for zeta in [Fraction(0), Fraction(1, 4), Fraction(2, 3), Fraction(1)]:
                with self.subTest(p=p, zeta=zeta):
                    replacement = (1 - zeta) * p
                    q = zeta * p / (1 - replacement)
                    self.assertEqual((1 - replacement) * (1 - q), 1 - p)
                    self.assertEqual((1 - replacement) * q + replacement, p)
                    self.assertEqual((1 - replacement) ** 2 * q * (1 - q),
                                     zeta * p * (1 - p))

    def test_fixed_weight_kernel_matches_incidence_expansion(self):
        for n, w in [(1, 0), (3, 1), (4, 2), (5, 3), (6, 4)]:
            sets = subsets(n, w)
            for zeta in [Fraction(0), Fraction(1, 4), Fraction(2, 3), Fraction(1)]:
                with self.subTest(n=n, w=w, zeta=zeta):
                    for left in sets:
                        for right in sets:
                            shared = len(left & right)
                            expanded = sum(
                                comb(shared, j) * zeta ** (w - j) * (1 - zeta) ** j
                                for j in range(shared + 1)
                            )
                            self.assertEqual(expanded, zeta ** (w - shared))
                    self.assertEqual(sum(
                        comb(w, j) * zeta ** (w - j) * (1 - zeta) ** j
                        for j in range(w + 1)
                    ), 1)

    def test_incidence_projector_has_constant_diagonal_and_thinned_mass(self):
        for n, w in [(3, 1), (4, 2), (5, 3), (6, 3)]:
            sets = subsets(n, w)
            size = len(sets)
            for k in range(1, w + 1):
                patterns = subsets(n, w - k)
                basis = inclusion_basis(sets, patterns)
                diagonal = projector_diagonal(basis, size)
                with self.subTest(n=n, w=w, k=k):
                    self.assertEqual(sum(diagonal), len(basis))
                    self.assertEqual(diagonal, [Fraction(len(basis), size)] * size)
                    self.assertLessEqual(diagonal[0], Fraction(len(patterns), size))

                    norms = [dot(vector, vector) for vector in basis]
                    for j in range(w - k + 1):
                        # Incidence columns from every lower level are in the range.
                        for pattern in subsets(n, j):
                            column = [int(pattern <= row) for row in sets]
                            projected_norm_squared = sum(
                                dot(column, vector) ** 2 / norm
                                for vector, norm in zip(basis, norms)
                            )
                            self.assertEqual(projected_norm_squared, dot(column, column))

                    for zeta in [Fraction(0), Fraction(1, 4), Fraction(2, 3), Fraction(1)]:
                        # Evaluate the density matrix entry by entry, independently
                        # of the expansion used to lower-bound its witness mass.
                        projected_mass = sum(
                            sum(
                                a * b * zeta ** (w - len(left & right))
                                for a, left in zip(vector, sets)
                                for b, right in zip(vector, sets)
                            ) / (size * norm)
                            for vector, norm in zip(basis, norms)
                        )
                        thinned_tail = sum(
                            comb(w, c) * zeta ** c * (1 - zeta) ** (w - c)
                            for c in range(k, w + 1)
                        )
                        self.assertGreaterEqual(projected_mass, thinned_tail)
                        self.assertLessEqual(projected_mass, 1)
                        if zeta in (0, 1):
                            expected_mass = diagonal[0] if zeta == 0 else 1
                            self.assertEqual(projected_mass, expected_mass)

    def test_poisson_quantile_and_finite_upper_bound_at_equality(self):
        with localcontext() as context:
            context.prec = 70
            mu = Decimal(1)
            target_mass = Decimal("0.99")
            for zeta, cutoff in [(Decimal(1), 4), (Decimal("0.25"), 2)]:
                rate = zeta * mu
                self.assertLess(poisson_cdf(rate, cutoff - 1), target_mass)
                self.assertGreaterEqual(poisson_cdf(rate, cutoff), target_mass)
                for n in [8, 32, 128]:
                    p = (1 - (-2 * mu / n).exp()) / 2
                    q = zeta * p / (1 - (1 - zeta) * p)
                    poisson_nonempty = 1 - (-rate / n).exp()
                    self.assertLessEqual(q, poisson_nonempty)
                    # Test the finite truncation at both an ordinary cutoff and
                    # the vacuum cutoff, each against its own limiting CDF.
                    for j in [0, cutoff]:
                        self.assertGreater(binomial_cdf(n, q, j), poisson_cdf(rate, j))


if __name__ == "__main__":
    unittest.main()
