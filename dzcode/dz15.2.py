from math import gcd


class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        # Simplify the fraction to its simplest form
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        # Multiplication of fractions: (a/b) * (c/d) = (a*c) / (b*d)
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        # Addition of fractions: (a/b) + (c/d) = (a*d + b*c) / (b*d)
        new_a = self.a * other.b + self.b * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        # Subtraction of fractions: (a/b) - (c/d) = (a*d - b*c) / (b*d)
        new_a = self.a * other.b - self.b * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        # Check if two fractions are equal: (a/b) == (c/d) if a*d == b*c
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        # Greater than comparison: (a/b) > (c/d) if a*d > b*c
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        # Less than comparison: (a/b) < (c/d) if a*d < b*c
        return self.a * other.b < self.b * other.a

    def __str__(self):
        # String representation of the fraction
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c)
f_d = f_b * f_a
assert str(f_d)
f_e = f_a - f_b
assert str(f_e)

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
