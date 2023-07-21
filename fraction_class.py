class Fraction(object):
    def __init__(self, numerator, denominator):
        #both must be int
        assert type(numerator) == int and type(denominator) == int
        self.n = numerator
        self.d = denominator
    def  __str__(self):
        #retutns a string representation of self
        return str(self.n)+"/"+str(self.d)
    def __add__(self, other):
        #sum method of 2 fractions
        top = self.n*other.d + self.d*other.n
        bott = self.d*other.d
        return Fraction(top, bott)
    def __sub__(self,  other):
        #subtraction method
        top = self.n*other.d - self.d*other.n
        bott = self.d*other.d
        return Fraction(top, bott)
    def __float__(self):
        #float reperesentation of fraciton
        return self.n/self.d
    def inverse(self):
        #inversion of fraction
        return Fraction(self.d, self.n)
    
    
a = Fraction(1, 4)
b = Fraction(2, 6)
c = a+b
print(c)
print(float(a))
print(Fraction.__float__(a))
print(a.inverse())
print(float(b.inverse()))