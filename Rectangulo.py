class Rectangulo:
    def __init__(self, p1=(0, 0), p2=(0, 0)):
        self.p1 = p1
        self.p2 = p2
    
    def base(self):
        return abs(self.p2[0] - self.p1[0])
    
    def altura(self):
        return abs(self.p2[1] - self.p1[1])
    
    def area(self):
        return self.base() * self.altura()