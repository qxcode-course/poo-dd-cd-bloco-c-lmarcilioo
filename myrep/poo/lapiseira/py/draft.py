class Lead:
    def __init__(self, thickness:float, hardness: str, size: int): 
        self.thickness = thickness
        self.hardness = hardness
        self.size = size


    def __str__(self):
        return f'{self.thickness}:{self.hardness}:{self.size}'

class Pencil:
    def __init__(self, thickness:float):
        self.thickness = thickness
        self.tip: Lead | None = None
        self.barrel: list[Lead] = []

    def __str__ (self):
        tambor = ''.join(f'[{lead}]' for lead in self.barrel)
        return f"calibre: {self.thickness}, bico: [{self.tip if self.tip is not None else ''}], tambor: <{tambor}>"
    
    def insert(self, thickness:float, hardness: str, size: int):
        if thickness != self.thickness:
            print("fail: calibre incompatível")
            return
        new = Lead(thickness, hardness, size)
        self.barrel.append(new)

    def pull (self):
        if self.tip is not None:
            print ("fail: ja existe grafite no bico")
        self.tip = self.barrel.pop(0)
    
    def remove (self):
        if self.tip is None:
            return
    
        if self.tip.size >10:
            self.barrel.insert(0, self.tip)
        self.tip = None

    def write (self):
        if self.tip is None:
            print ('fail: nao existe grafite no bico')
            return
        
        if self.tip.size <= 10:
            print('fail: tamanho insuficiente')
            return
    
        gasto = {'HB':1, '2B': 2, '4B':4, '6B':6}[self.tip.hardness]

        utilizavel = self.tip.size - 10
        

        if utilizavel < gasto:
            self.tip.size = 10
            print('fail: folha incompleta')
            return
        
        self.tip.size -= gasto

    
           


def main():
    grafite = Pencil
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "init":
            thickness = float(args[1])
            grafite = Pencil(thickness)
        if args [0] == "show":
            print(grafite)
        if args [0] == 'insert':
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite.insert(thickness, hardness, size)
        if args [0] == 'pull':
            grafite.pull()
        if args [0] == 'remove':
            grafite.remove()
        if args [0] == 'write':
            grafite.write()

main()