import csv

# define a classe No
class No:
    def __init__(self, x, h):
        self.valor = x
        self.esq = None
        self.dir = None
        self.altura = h

# define a função de inserir nós com sua altura
def insertNode(no, x, h):
    if no is None:
        no = No(x,h)
        return no
    h += 1
    if x < no.valor:
        no.esq = insertNode(no.esq, x, h)
    else:
        no.dir = insertNode(no.dir, x, h)
    return no

# define a função busca pelo nó com maior altura
def searchMaxH(no, h):
    maxH = h
    if no:
        maxHEsq = searchMaxH(no.esq, maxH)

        maxHDir = searchMaxH(no.dir, maxH)

        maxH = max(no.altura, maxHEsq, maxHDir)
    return maxH

# define a função que realiza a busca por nós que possuam a maior altura
def searchByH(no, h):
    if no:
        if no.altura == h:    
            return no.valor
        
        valoresq = searchByH(no.esq, h)
        if valoresq:
            return valoresq
        
        valordir = searchByH(no.dir, h)
        if valordir:
            return valordir
    
    return None

# nome do arquivo CSV a ser utilizado
arquivo = 'cem.csv'

# código para ler os valores do arquivo CSV e preencher a árvore
with open(arquivo, 'r') as arquivocsv:
    leitor = csv.reader(arquivocsv)
    for linha in leitor:
        raizatual = No(int(linha[0]),1)
        for x in range(1,len(linha)):
            raizatual = insertNode(raizatual,int(linha[x]),1)

maiorH = searchMaxH(raizatual,1)
print("Maior altura da árvore: ", maiorH)

print("Valor com maior altura: ", searchByH(raizatual, maiorH))
