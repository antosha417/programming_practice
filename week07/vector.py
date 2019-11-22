class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __str__(self):
        return "Координатное представление вектора:" + '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __radd__(self, other):
        return self.x + other.x, self.y + other.y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __rsub__(self, other):
        return other.x - self.x, other.y - self.y

    def __neg__(self):
        return self.x, self.y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __bool__(self):
        return self.x != 0 and self.y != 0

    def __abs__(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** (1 / 2)


if __name__ == '__main__':
    a = Vector(3, 4)
    b = Vector(2, 3)
    print(abs(a))

