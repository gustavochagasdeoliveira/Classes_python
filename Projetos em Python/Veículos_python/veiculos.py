class Veiculo:
    def __init__(self, marca = "Desconhecida", modelo = "", ano = 2000):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def mostrar_info(self):
        print (f"Marca: {self.marca}")
        print (f"Modelo: {self.modelo}")
        print (f"Ano: {self.ano}")

class Carro (Veiculo):
    
    def __init__(self, marca="Desconhecida", modelo="", ano=2000, portas = 4):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def mostrar_info(self):
        super().mostrar_info()
        print (f"Portas: {self.portas}")
    
class Moto (Veiculo):

    def __init__(self, marca="Desconhecida", modelo="", ano=2000, cilindradas = 150):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def mostrar_info(self):
        super().mostrar_info()
        print (f"Cilindradas: {self.cilindradas}cc")

v1 = Carro(marca ="Ferrari", modelo ="LaFerrari", ano = 2018)
v1.mostrar_info()

v2 = Moto(marca = "BMW", modelo = "S1000", ano = 2024, cilindradas = 1000)
v2.mostrar_info()