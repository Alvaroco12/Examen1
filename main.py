from Punto import Punto
from Rectangulo import Rectangulo

if __name__ == "__main__":
    punto = Punto()

    A = punto.crear(2, 3)
    B = punto.crear(5, 5)
    C = punto.crear(-3, -1)
    D = punto.crear()

    print(A)
    print(B)
    print(C)
    print(D)

    print(A.cuadrante())
    print(B.cuadrante())
    print(D.cuadrante())

    print(A.vector(B))
    print(B.vector(A))


    rect = Rectangulo(A, B)
    print(rect.base())
    print(rect.altura())
    print(rect.area())