class Vector:
    def __init__(self, s):
        self.x = list(map(float, s.split(',')))[0]
        self.y = list(map(float, s.split(',')))[1]
    def __add__(self, other):
        return Vector(str(self.x + other.x)+','+str(self.y + other.y))
    def __sub__(self, other):
        return Vector(str(self.x - other.x)+','+str(self.y - other.y))
    def __mul__(self, other):
        return Vector(str(self.x*other.x) + ',' + str(self.y*other.y))
    def l(vec):
        return float((vec.x**2+vec.y**2)**0.5)
N = int(input())
V = []
X = []
Y = []
for i in range(N):
    V.append(Vector(str(input())))
    X.append(V[i].x)
    Y.append(V[i].y)
print(sum(X)/len(X), sum(Y)/len(Y))