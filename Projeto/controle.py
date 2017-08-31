from palavra import *
from lista import Lista


class Controle:
    def __init__(self):
        self.numeroTermos = 0
        self.termos = list()
        self.dadosCarregados = True
    
    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False
    
    #TODO: PRONTO
    def __firstIndexOf(self,prefixo):
            
        l = self.termos
        inicio=0
        fim=self.numeroTermos-1
        def buscabi(l, prefixo, inicio, fim):
            pos = (inicio + fim)//2

            if pos < 0 or pos >=len(l):
                return False
            
            if prefixo == l[pos][0][:len(prefixo)] and prefixo != l[pos-1][0][:len(prefixo)]:
                return pos
            
            elif prefixo > l[pos][0][:len(prefixo)]:
                inicio = pos+1
                return buscabi(l,prefixo,inicio,fim)

            else:
                fim = pos-1
                return buscabi(l,prefixo,inicio,fim)
        try:    
            firstIndex = buscabi(l,prefixo, inicio, fim)
        except:
            return fim-1

        return firstIndex
    
    #TODO: PRONTO
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1        
        pos = -1
        first = self.__firstIndexOf(prefixo)
        l = self.termos[first:]
        for x in l:
            if x[0][:len(prefixo)] == prefixo:
                first += 1           
            else:
                break
        pos += first   
        return pos
     
    #TODO: PRONTO   
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()
        
        abreArquivo = open(filename, encoding="utf8")
        abreArquivo = list(abreArquivo)
        for x in abreArquivo[1:]:
                x = x.replace("\n", "")
                x = x.strip(" ")
                x = x.split('\t')
                aux = x[0]
                x[0] = x[1]
                x[1] = int(aux)
                x = (x[0],x[1])
                self.termos.append(x)

        self.numeroTermos = int(abreArquivo[0].replace("\n","")) 
        self.termos.sort()
        self.dadosCarregados = True
    
    #TODO: PRONTO    
    def find(self, prefixo, qtd):
        listaEncadeada = Lista()
        first = self.__firstIndexOf(prefixo)
        last = self.__lastIndexOf(prefixo)
        primeiraPalavra = True
        if first == last:
            first = first-1
        count = 1
        for palavra in self.termos[first-1:last+1]:
            if prefixo == palavra[0][:len(prefixo)]:
                palavra = Palavra(palavra[0],palavra[1])
                if primeiraPalavra:
                    listaEncadeada.inserirOrdenado((palavra.peso, palavra.termo), comparaPorPeso(palavra, palavra))
                    palavraAntiga = listaEncadeada.ultimo.item
                    palavraAntiga = Palavra(palavraAntiga[1],palavraAntiga[0])
                    primeiraPalavra=False
                else:
                    if count < qtd:
                        listaEncadeada.inserirOrdenado((palavra.peso, palavra.termo), comparaPorPeso(palavra,palavraAntiga))
                        count += 1
                    else:
                        if comparaPorPeso(palavra,palavraAntiga) > 0:
                            if listaEncadeada.tamanho > 1:
                                listaEncadeada.removerFim()
                            palavraAntiga = listaEncadeada.ultimo.item
                            palavraAntiga = Palavra(palavraAntiga[1],palavraAntiga[0])
                            listaEncadeada.inserirOrdenado((palavra.peso, palavra.termo), comparaPorPeso(palavra,palavraAntiga))
                        
        aux = listaEncadeada.primeiro
        if aux is None or listaEncadeada.tamanho == 0:
            return 'Palavra não encontrada'

        contadorPrint = 0
        stringPrint = ''
        while aux != None and contadorPrint < qtd:
            stringPrint += aux.item[1] + '\n'
            aux = aux.prox
            contadorPrint += 1
            
        return stringPrint
