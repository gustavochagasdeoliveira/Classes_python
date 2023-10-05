class Produtos:
    def __init__(self, codigo = "", nome = "", preco = 5.00):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        print (f"Código do produto: {self.codigo}")
        print (f"Nome do produto: {self.nome}")
        print (f"Preco do produto: {self.preco}")

class Produto_eletronico (Produtos):
    def __init__(self, codigo="", nome="", preco=5, garantia = 12):
        super().__init__(codigo, nome, preco)
        self.garantia = garantia

    def exibir_info(self):
        super().exibir_info()
        print (f"Garantia do porduto de: {self.garantia} meses")

class Produto_alimenticio (Produtos):
    def __init__(self, codigo="", nome="", preco=5, validade = ""):
        super().__init__(codigo, nome, preco)
        self.validade = validade

    def exibir_info(self):
        super().exibir_info()
        print (f"Data de validade do produto: {self.validade}")

produto1 = Produto_eletronico (codigo = "123", nome = "SmartTv", preco = 4500.45, garantia = 24)
produto1.exibir_info()

produto2 = Produto_alimenticio (codigo = "321", nome = "Banana", preco = 5.25, validade = "12/02/2025")
produto2.exibir_info()