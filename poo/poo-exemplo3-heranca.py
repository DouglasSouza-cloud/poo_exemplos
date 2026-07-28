# HERANÇA

# SUPONHA QUE EXISTAM VÁRIOS VEÍCULOS, TODOS POSSUEM:
# RODAS, ACELERAR E FREAR. LOGO, NÃO FAZ SENTIDO REPETIR O CÓDIGO
# PODEMOS CRIAR UMA CLASSE GERAL E DEPOIS FAZER OUTRAS CLASSES HERDAREM DELA

# CLASSE PAI (VEÍCULO)
class Veiculo:

    def __init__(self, rodas):

        self.rodas = rodas

    def acelerar(self):

        print(f"O {self.modelo} DE {self.rodas} RODAS ACELEROU! :)")

# CLASSE FILHO (CARRO)
# O CARRO HERDA TUDO DA CLASSE "VEÍCULO"
class carro(Veiculo): # É OBRIGATÓRIO A DECLARAÇÃO CLASS FILHO (NOME DA CLASSE PAI)
# HERANÇA MULTIPLA> CLASS CARROACOMBUSTÃO(CARRO, VEÍCULO, ...,)
    def __init__(self, marca, modelo):

        super().__init__(4) # ESSA LINHAEXECUTA O CONSTRUTOR DA CLASSE PAI

        self.marca = marca

        self.modelo = modelo
        print(f"CRIANDO UM CARRO {self.modelo} COM {self.rodas} RODAS. :)")
carro1 = carro("TOYOTA","SUPRA MK4")
print()
carro1.acelerar()
