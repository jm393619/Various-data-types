class Fraction:

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"Fraction: (numerator: {self.numerator}, denominator: {self.denominator})"
