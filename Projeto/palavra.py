class Palavra:
    def __init__(self,termo="",peso=-1):
        self.termo = termo
        self.peso = peso
    
    #TODO: PRONTO
    def __lt__(self,other):
        return self.termo < other.termo
    
    def __str__(self):
        return "{0}, {1}".format(self.termo,self.peso)
    
    def __repr__(self):
        return self.__str__()

#TODO: PRONTO      
def comparaPorPrefixo(palavra, prefixo):
        if palavra[:len(prefixo)] > prefixo:
                return 1
        elif palavra[:len(prefixo)] > prefixo:
                return 0
        else:
                return -1

        

#TODO: PRONTO
def comparaPorPeso(palavra1, palavra2):
        if palavra1.peso > palavra2.peso:
                return 1

        elif palavra1.peso == palavra2.peso:
                return 0
        else:
                return -1



