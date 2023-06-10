class Fraction:

    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError('Numerator should be of type int.')
        if not isinstance(denominator, int):
            raise TypeError('Numerator should be of type int.')

        if denominator == 0:
            raise ValueError("Denominator can't be equal to zero.")

        a, b = abs(numerator), abs(denominator)

        _gcd = self.gcd(a, b)

        if _gcd != 1:
            numerator //= _gcd
            denominator //= _gcd

        self.numerator = numerator if denominator > 0 else -numerator
        self.denominator = abs(denominator)

    def __repr__(self):
        return f"Fraction: (num: {self.numerator}, den: {self.denominator})"

    @staticmethod
    def gcd(a, b):

        if not b:
            return a
        else:
            return Fraction.gcd(b, a % b)

    def reduce(self):

        _gcd = self.gcd(abs(self.numerator), abs(self.denominator))

        return Fraction(self.numerator // _gcd, self.denominator // _gcd)

    def __eq__(self, other):

        s = self.reduce()
        o = other.reduce()

        return s.numerator == o.numerator and s.denominator == o.denominator

    def __add__(self, other):

        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __sub__(self, other):

        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __mul__(self, other):

        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator

        return Fraction(num, den)

    def __abs__(self):

        num = abs(self.numerator)
        den = self.denominator

        return Fraction(num, den)

    def __neg__(self):

        num = - self.numerator
        den = self.denominator

        return Fraction(num, den)

    def __bool__(self):
        return bool(self.numerator)

    def __iadd__(self, other):

        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator

        self.numerator = num
        self.denominator = den

        return self

    def __isub__(self, other):

        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator

        self.numerator = num
        self.denominator = den

        return self

    def __imul__(self, other):

        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        self.numerator = num
        self.denominator = den

        return self

    def __itruediv__(self, other):

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator

        self.numerator = num
        self.denominator = den

        return self

    def __int__(self):

        if self.numerator < 0:
            return -(-self.numerator // self.denominator)
        else:
            return self.numerator // self.denominator

    def __float__(self):

        return round(self.numerator / self.denominator, 6)

    def __gt__(self, other):

        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):

        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __floordiv__(self, other):

        return self.numerator * other.denominator // other.numerator * self.denominator


