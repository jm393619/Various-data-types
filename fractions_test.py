from main import Fraction
import unittest


class TestOne(unittest.TestCase):

    def test_gcd(self):

        cases = [
            (12, 18, 6),
            (18, 12, 6),
            (10, 1, 1),
            (1, 10, 1),
            (10, 10, 10),
            (24, 16, 8),
            (144, 642, 6)
        ]

        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(Fraction.gcd(x, y), result)

    def test_reduce(self):
        f1 = Fraction(2, 4)
        f2 = Fraction(4, 6)
        f3 = Fraction(2, 6)
        f4 = Fraction(-3, 6)

        cases = [
            (f1, Fraction(1, 2)),
            (f2, Fraction(2, 3)),
            (f3, Fraction(1, 3)),
            (f4, Fraction(-1, 2))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(x, result)


class TestTwo(unittest.TestCase):

    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 3)
        self.f3 = Fraction(3, 4)

    def test_add(self):

        cases = [
            (self.f1, self.f2, Fraction(7, 6)),
            (self.f1, self.f3, Fraction(5, 4)),
            (self.f2, self.f3, Fraction(17, 12))

        ]

        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(x + y, result)

    def test_sub(self):

        cases = [
            (self.f1, self.f2, Fraction(-1, 6)),
            (self.f1, self.f3, Fraction(-1, 4)),
            (self.f2, self.f3, Fraction(-1, 12)),
            (self.f2, self.f1, Fraction(1, 6)),
            (self.f3, self.f1, Fraction(1, 4)),
            (self.f3, self.f2, Fraction(1, 12))
        ]

        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(x - y, result)

    def test_mul(self):

        cases = [
            (self.f1, self.f2, Fraction(1, 3)),
            (self.f1, self.f3, Fraction(3, 8)),
            (self.f2, self.f3, Fraction(1, 2)),
        ]

        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(x * y, result)

    def test_truediv(self):

        cases = [
            (self.f1, self.f2, Fraction(3, 4)),
            (self.f1, self.f3, Fraction(2, 3)),
            (self.f2, self.f3, Fraction(8, 9)),
        ]

        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(x / y, result)


class TestThree(unittest.TestCase):

    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 3)
        self.f3 = Fraction(3, 4)

    def test_add(self):

        cases = [
            (self.f1, Fraction(1, 1)),
            (self.f2, Fraction(7, 6)),
            (self.f3, Fraction(5, 4))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                x += Fraction(1, 2)
                self.assertEqual(x, result)

    def test_isub(self):

        cases = [
            (self.f1, Fraction(0, 1)),
            (self.f2, Fraction(1, 6)),
            (self.f3, Fraction(1, 4))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                x -= Fraction(1, 2)
                self.assertEqual(x, result)

    def test_imul(self):

        cases = [
            (self.f1, Fraction(1, 3)),
            (self.f2, Fraction(4, 9)),
            (self.f3, Fraction(1, 2))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                x *= Fraction(2, 3)
                self.assertEqual(x, result)

    def test_itruediv(self):

        cases = [
            (self.f1, Fraction(3, 4)),
            (self.f2, Fraction(1, 1)),
            (self.f3, Fraction(9, 8))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                x /= Fraction(2, 3)
                self.assertEqual(x, result)


class TestFour(unittest.TestCase):

    def setUp(self):
        self.f1 = Fraction(-1, 2)
        self.f2 = Fraction(2, 3)
        self.f3 = Fraction(3, -4)
        self.f4 = Fraction(0, 1)

    def test_abs(self):
        cases = [
            (self.f1, Fraction(1, 2)),
            (self.f2, Fraction(2, 3)),
            (self.f3, Fraction(3, 4))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(abs(x), result)

    def test_denominator_should_be_always_positive(self):
        self.assertEqual(self.f3.denominator, 4)
        self.assertEqual(self.f3.numerator, -3)

    def test_neg(self):
        cases = [
            (self.f1, Fraction(1, 2)),
            (self.f2, Fraction(-2, 3)),
            (self.f3, Fraction(3, 4))
        ]

        for x, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(-x, result)

    def test_bool(self):
        self.assertTrue(self.f1)
        self.assertFalse(self.f4)
