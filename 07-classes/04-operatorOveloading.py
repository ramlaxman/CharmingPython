"""
Addition 	p1 + p2 	p1.__add__(p2)
Subtraction 	p1 - p2 	p1.__sub__(p2)
Multiplication 	p1 * p2 	p1.__mul__(p2)
Power 	p1 ** p2 	p1.__pow__(p2)
Division 	p1 / p2 	p1.__truediv__(p2)
Floor Division 	p1 // p2 	p1.__floordiv__(p2)
Remainder (modulo) 	p1 % p2 	p1.__mod__(p2)
Bitwise Left Shift 	p1 << p2 	p1.__lshift__(p2)
Bitwise Right Shift 	p1 >> p2 	p1.__rshift__(p2)
Bitwise AND 	p1 & p2 	p1.__and__(p2)
Bitwise OR 	p1 | p2 	p1.__or__(p2)
Bitwise XOR 	p1 ^ p2 	p1.__xor__(p2)
Bitwise NOT 	~p1 	p1.__invert__()
"""


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)