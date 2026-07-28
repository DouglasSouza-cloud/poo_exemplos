# CLASSE EM PYTHON
class carro:
    # MÉTODO CONSTRUTOR
    def __init__ (self, marca, modelo, ano):
        # DEF INIT É O OBJETO CONSTRUTOR, SERÁ EXECUTADO SEMPRE
        #NA CRIAÇÃO DE OBJETO
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    # MÉTODO DA CLASSE
    def exibir_dados(self):
        print("--- DADOS DO CARRO ---")
        print(f"MARCA: {self.marca}")
        print(f"MODELO: {self.modelo}")
        print(f"ANO: {self.ano}")

# CRIANDO OBJETOS
carro1 = carro ("FORD", "MUSTANG", 1970)
carro2 = carro ("NISSAN", "GTR R32", 1980)
carro3 = carro ("DODGE", "CHALLENGER", 1970)
carro4 = carro ("DODGE", "HELLCAT", 1960)
# CHAMADA DO OBJETO E MÉTODO
carro1.exibir_dados()
print()
carro2.exibir_dados()
print()
carro3.exibir_dados()
print()
carro4.exibir_dados()
print()

