# INTEGRANDO OS 4 PILARES DO POO
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def mostrar_dados(self):
        print(f"FUNCIONÁRIO: {self.nome}")
    
    def calcular_bonus(self):
        self.__salario * 0.10 + self.salario

class Gerente (Funcionario):
    def calcular_bonus(self):
        return 5000
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return 2000
    
gerente = Gerente("LIANDRO", 1000000)
dev = Desenvolvedor("VALENTIM", 100)

gerente.mostrar_dados()
print("BÔNUS: ", gerente.calcular_bonus())
print("-"*30)
dev.mostrar_dados()
dev.calcular_bonus()

"""
CONCEITO ----------
CLASSE ------------ FUNC, GER, DEV
OBJETO ------------ GERENTE1, DEV1
METODO ------------ MOSTRAR)DADOS()
ATRIBUTO ---------- NOME, __SALARIO
ENCAPSULAMENTO ---- __SALARIO
HERANCA ----------- GERENTE (FUNCIONARIO)
POLIMOFISMO ------- CALCULAR_BONUS() --DIFERENTE EM CADA CLASSE
"""