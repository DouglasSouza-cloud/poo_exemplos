# O QUE É ENCAPSULAMENTO?
# IMAGINE UMA CONTA BANCÁRIA E UM SALDO DE 1000000 DE REAIS,
# POR ACASO É POSSÍVEL ALTERAR ESSE VALOR DE QUALQUER FORMA,
# OU EM QUALQUER PARTE DO SISTEMA?

class contabancaria():

    def __init__ (self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        # "__" INDICA QUE O ATRIBUTO É PRIVATE

    def depositar(self, valor):
        if valor > 0:

            self.__saldo += valor

            print("DEPÓSITO REALIZADO. :)")

        else:

            print("VALOR INVÁLIDO. >:(")

    def sacarvalor(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("SAQUE REALIZADO COM SUCESSO! :)")
        else: 
            print("SALDO INSUFICIENTE. :(")
        


    def mostrarsaldo(self):
        print(f"SALDO ATUAL: R${self.__saldo:.2f}")

conta1 = contabancaria ("Alberto",1200) 
conta2 = contabancaria ("Alberto JR", 600) 
conta3 = contabancaria ("Albertão", 3001) 
conta4 = contabancaria ("Alfredo Berto", 6000) 

conta1.mostrarsaldo()
print()
conta1.depositar(100)
print()
conta1.mostrarsaldo()
print()
conta1.sacarvalor(100)
print()
conta1.mostrarsaldo()

conta1.__saldo = 1200
print()
conta1.mostrarsaldo
