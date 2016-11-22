class Vector:
    def __init__(self, s):
        self.x = float(list(map(float, s.split(',')))[0])
        self.y = float(list(map(float, s.split(',')))[1])
    def __add__(self, other):
        return Vector(str(self.x + other.x)+','+str(self.y + other.y))
    def __sub__(self, other):
        return Vector(str(self.x - other.x)+','+str(self.y - other.y))
    def __mul__(self, other):
        return float((self.x)*(other.x) + (self.y)*(other.y))
A = Vector('1,2')
B = Vector('3,4')
C = A*B
print(C)