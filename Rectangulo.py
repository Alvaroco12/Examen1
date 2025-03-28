class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p2.x - self.p1.x)  # Cambiar de self.p2[0] a self.p2.x

    def altura(self):
        return abs(self.p2.y - self.p1.y)  # Cambiar de self.p2[1] a self.p2.y

    def area(self):
        return self.base() * self.altura()