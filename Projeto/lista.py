class No:
    def __init__(self,item=None,ant=None,prox=None):
        self.item = item
        self.ant = ant
        self.prox = prox
    
class Lista:

    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0
    
    def size(self):
        return self.tamanho

    #TODO: implemente
    def inserirOrdenado(self, item, cmp):    
        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''
        if self.tamanho==0:
            self.primeiro = No(item,None,None)
            self.ultimo = self.primeiro
            self.tamanho +=1
            return

        if cmp > 0:
            if self.primeiro.item[0] < item[0]:
                aux = self.primeiro
                self.primeiro = No(item,None,aux)
                self.primeiro.prox.ant = self.primeiro
                self.tamanho += 1
                return
                
            ante = self.ultimo
            atual = self.ultimo.ant
            while atual !=None and atual.item[0] < item[0]:
                ante = atual
                atual = ante.ant
            
            itemInsercao = No(item,atual, atual.prox)
            atual.prox.ant = itemInsercao
            atual.prox = itemInsercao
            self.tamanho+=1
            return

        else:
            itemInsercao = No(item,self.ultimo,None)
            self.ultimo.prox = itemInsercao
            self.ultimo = itemInsercao
            self.tamanho +=1
            return
                        

#TODO: COMPLETO    
    def removerFim(self):
        if (self.size() == 0):
            return None

        elif (self.size() == 1):
            ultimoAntigoNo = self.ultimo
            self.primeiro = self.ultimo = No()
            self.tamanho -= 1
            
            itemRemovido = ultimoAntigoNo.item
            del ultimoAntigoNo
            
            return itemRemovido

        ultimoAntigoNo = self.ultimo
        novoUltimoNo = self.ultimo.ant
        novoUltimoNo.prox = None
        ultimoAntigoNo.ant = None
        self.ultimo = novoUltimoNo
        self.tamanho -= 1

        itemRemovido = ultimoAntigoNo.item
        del ultimoAntigoNo

        return itemRemovido

    #TODO: implemente        
    def __str__(self):
        stringPrint = ''
        aux = self.primeiro
        while aux != None:
            stringPrint += aux.item[1] + '\n'
            aux = aux.prox
        return stringPrint
    

    def __repr__(self):
        stringPrint = ''
        aux = self.primeiro
        while aux != None:
            stringPrint += aux.item[1] + '\n'
            aux = aux.prox
        return stringPrint
