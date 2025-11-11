class Pessoa:
    def __init__ (self, nome: str):
        self.__nome = nome

    def __str__ (self):
        return self.__nome
    
    def getNome(self):
        return self.__nome
    

class Market:
    def __init__ (self, numCaixas: int):
        self.caixas: list[Pessoa | None] = []
        self.espera: list[Pessoa] = []
        for _ in range (numCaixas):
            self.caixas.append(None)

    def __str__(self):
        caixas = ", ".join(["-----" if x is None else str (x) for x in self.caixas])
        espera = ", ".join([str (x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    def arrive (self, person: Pessoa):
        self.espera.append(person)

    def call (self, index: int):
        if self.caixas[index] is not None:
            print ("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera[0]
        del self.espera [0]

    def finish (self, index: int):
         if index <0 or index >= len(self.caixas):
            print ("fail: caixa inexistente")
            return
         if self.caixas [index] is None:
             print ("fail: caixa vazio")
         self.caixas[index] = None

def main():
    budega = Market
    while True:
        line = input()
        print("$" + line)
        args: list [str] = line.split(" ")
        if args [0] == "end":
            break
        if args [0] == "init":
            budega = Market(numCaixas=int(args[1]))
        if args [0] == "show":
            print(budega)
        if args [0] == "arrive":
            pessoa = Pessoa(args[1])
            budega.arrive(pessoa)
        if args [0] == "call":
            index = int(args[1])
            budega.call (index)
        if args [0] == "finish":
            index = int(args[1])
            budega.finish(index)



main()