import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"

    # Métodos de clase
    @classmethod
    def crear(cls, x=0, y=0):
        return cls(x, y)

    # Método para determinar el cuadrante
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"
        
    # Metodo vector
    def vector(self, p):
        return Punto(p.x - self.x, p.y - self.y) # llama a la funcion punto y le pasa como parametro la diferencia de las coordenadas
    
    # Método distancia
    def distancia(self, p):
        distancia = math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
        print(f"La distancia entre los puntos ({self.x}, {self.y}) y ({p.x}, {p.y}) es: {distancia}")
        return distancia