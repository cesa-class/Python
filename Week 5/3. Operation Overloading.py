class Rational:
    def __init__(self, up, down):
        self.up = up
        self.down = down
    def __str__(self):
        return '{}/{}  {}'.format(self.up, self.down,
                                  self.up / self.down)
    def __add__(self, other):
        return Kasri(self.down * other.up + self.up * other.down,
                     self.down * other.down)
    def __sub__(self, other):
        return Kasri(other.down * self.up - self.down * other.up,
                     self.down * other.down)
    def __div__(self, other):
        return Kasri(other.down * self.up, self.down * other.up)    

    def __mul__(self, other):
        return Kasri(self.up * other.up, self.down * other.down)



if __name__ == "__main__":
    a = Rational(1, 2)
    b = Rational(3, 5)
    c = a + b
    print(a, b)
    print(c)
    d = a - b
    print(d)
    e = a * b
    print(e)
    f = a / b
    print(f)