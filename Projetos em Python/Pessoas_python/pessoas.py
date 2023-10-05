class Pessoas:
    def __init__(self, nome = "", idade = 18, sexo = ""):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def apresentar (self):
        print (f"Nome: {self.nome}")
        print (f"Idade: {self.idade}")
        print (f"Sexo: {self.sexo}")
    
class Aluno (Pessoas):
    def __init__(self, nome = "", idade = 18, sexo = "", matricula = ""):
        super().__init__(nome, idade, sexo)
        self.matricula = matricula

    def apresentar(self):
        super().apresentar( )
        print (f"Matrícula: {self.matricula}")

class Professor (Pessoas):
    def __init__(self, nome="", idade = 18, sexo="", disciplina = ""):
        super().__init__(nome, idade, sexo)
        self.disciplina = disciplina
    
    def apresentar(self):
        super().apresentar()
        print (f"Disciplina: {self.disciplina}")

p1 = Aluno (nome = "Gustavo Chagas de Oliveira", idade = 19, sexo = "M", matricula = "010101")
p1.apresentar()

p2 = Professor (nome = "Roberta Silva", idade = 34, sexo = "F", disciplina = "Matemática")
p2.apresentar()