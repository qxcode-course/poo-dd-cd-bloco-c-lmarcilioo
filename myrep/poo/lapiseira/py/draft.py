class Lead:
    def __init__(self, thickness:float, size: int, hardness: str): 
        self.thickness = thickness
        self.size = size
        self.hardness = hardness

    #def __str__(self):
        #return 

class Pencil:
    def __init__(self, thickness:float, tip: Lead | None, barrel: Lead):
        self.thickness = thickness
        self.tip = tip
        self.barrel = barrel

    def __str__ (self):
        return f"calibre: {self.thickness}, bico: [{self.tip}], tambor: <{self.barrel}>"
    
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
            tip = (args[2])
            barrel = (args[3])
            grafite = Pencil(thickness, tip, barrel)
        if args [0] == "show":
            print(grafite)

main()