from fractions import Fraction
class Fractions:
    def __init__(self, num):
        self.num = num


    def __add__(self, other):
        if isinstance(other, Fractions):
            return self.num + other.num
        elif isinstance(other, (int, float)):
            return self.num + other
        raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Fractions):
            return self.num * other.num
        elif isinstance(other, (int, float)):
            return self.num * other
        raise NotImplemented

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, Fractions):
            return self.num - other.num
        elif isinstance(other, (int, float)):
            return self.num - other
        raise NotImplemented

    def __rsub__(self, other):
        return self - other

    def __truediv__(self, other):
        if isinstance(other, Fractions):
            return self.num / other.num
        elif isinstance(other, (int, float)):
            return self.num / other
        raise NotImplemented

    def __rtruediv__(self, other):
        return self / other


class Fract(Fractions):
    def __init__(self, numerator, denominator):
        super().__init__(num=0)
        self.numerator = numerator
        self.denominator = denominator

    def convert(self):
        return Fraction(self.numerator,self.denominator)
