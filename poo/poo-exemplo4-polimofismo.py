# POLIMOFISMO

# OBJETOS DIFERENTES PODEM RESPONDER AO MESMO MÉTODO
# TODOS POSSUEM O MÉTODO: FALAR
# MAS CADA UM FALA DIFERENTE > EXEMPLO: CACHORROS

class cachorro:
    #def __init__(self):
    def falar(self):
        print("AU AU, AU AU, AU AU :b")
class gato:
    def falar(self):
        print("MIAU MIAU, MIAU MIAU :3")
class vaca:
    def falar(self):
        print("MUUUH MUUUH, MUUUH MUUUH >:)")
def emitir_som(animal):
    animal.falar()

cachorro = cachorro()
gato = gato()
vaca = vaca()

emitir_som(cachorro)
emitir_som(gato)
emitir_som(vaca)
