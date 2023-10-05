class Figura:
    def __init__(self, area = 1.5):
        self._area = area
    
class Retangulo (Figura):
    def __init__(self, base = 1.0, altura = 1.0):
        self._area = base * altura

    def mostrar_area(self):
        print (f"A area do retangulo e de {self._area} m²")

class Circulo (Figura):
    def __init__(self, area = 1.0, raio = 1.5):
        super().__init__(area)
        self._area = 3.14 * (raio * raio)

    def mostrar_area(self):
        print (f"A area do circulo e de {self._area} m²")    

class TrianguloRetangulo (Figura):
    def __init__(self, area=1.5, base = 2.0, altura = 2.0):
        super().__init__(area)
        self._area = base * altura

    def mostrar_area(self):
        print (f"A area do Triangulo Retangulo e de {self._area} m²")




f1 = Retangulo(base = 2.5, altura = 5.0)
f1.mostrar_area()

f2 = Circulo(raio = 5.0)
f2.mostrar_area()

f3 = TrianguloRetangulo(base = 4.0, altura = 5.5)
f3.mostrar_area()