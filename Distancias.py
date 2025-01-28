class DistanciaPuntos:

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    distancia = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcular_distancia(self):
        self.distancia = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print("La distancia entre los puntos es: {:.2f}".format(self.distancia))

def main():
    x1 = int(input("Ingresa un número para x1: "))
    y1 = int(input("Ingresa un número para y1: "))
    x2 = int(input("Ingresa un número para x2: "))
    y2 = int(input("Ingresa un número para y2: "))

    obj = DistanciaPuntos(x1, y1, x2, y2)
    obj.calcular_distancia()

if __name__ == "__main__":
    main()
