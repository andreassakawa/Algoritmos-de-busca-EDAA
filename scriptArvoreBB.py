import random
import csv
import time
import tracemalloc
import statistics
import gc

# código utilizado para gerar vetores com número de 1 a n
#vetor = list(range(1,5,1))

# código utilizado para embaralhar os números no vetor
#random.shuffle(vetor)

# código utilizado para escrever o vetor em arquivos CSV
#with open(arquivo, 'w', newline='') as arquivocsv:
    #csvwriter = csv.writer(arquivocsv)

    #csvwriter.writerow(vetor)

# define classe No
class No:
    def __init__(self, x):
        self.valor = x
        self.esq = None
        self.dir = None

# Função que insere nó na árvore
def insertNode(no, x):
    if no is None:
        no = No(x)
        return no

    if x < no.valor:
        no.esq = insertNode(no.esq, x)
    else:
        no.dir = insertNode(no.dir, x)
    return no

# Função que realiza a busca na árvore
def searchData(no, x):
    comparacoes = 1
    if no.valor == x:    
        #print("Valor encontrado!")
        return comparacoes
    
    while no is not None:
        comparacoes += 1
        if x > no.valor:
            no = no.dir
        elif x < no.valor:
            no = no.esq
        else:
            #print('Valor encontrado!')
            return comparacoes
        
    #print('Valor não encontrado!')
    return comparacoes

# Função que cria o vetor a partir da base de dados CSV e realiza a busca 
#uma quantidade n de vezes
# - Recebe: (nome do arquivo da base de dados)
def buscaSequencial(arquivo):
    # inicia o monitoramento de memória
    tracemalloc.start()

    #snapshotini = tracemalloc.take_snapshot()

    # nome do arquivo CSV a ser utilizado
    nomearquivo = arquivo

    # código para ler os valores do arquivo CSV e preencher a árvore
    with open(nomearquivo, 'r') as arquivocsv:
        leitor = csv.reader(arquivocsv)
        for linha in leitor:
            raizatual = No(int(linha[0]))
            for x in range(1,len(linha)):
                raizatual = insertNode(raizatual,int(linha[x]))
            entrada = int(random.choice(linha))

    #snapshotmei = tracemalloc.take_snapshot()

    # define valor a ser buscado
    #entrada = int(input())
    #entrada = 12415

    # código que salva o tempo inicial
    tempoinicial = time.time()

    resultado = searchData(raizatual,entrada)

    # imprime a diferença entre o tempo atual e o inicial
    #print("Tempo busca binária: %s segundos" % (time.time()-tempoinicial))

    # delay (em segundos)
    time.sleep(0.001)
    tempofinal = time.time() - tempoinicial

    #print("Número de comparações: ", resultado)

    #snapshotfin = tracemalloc.take_snapshot()

    #memoriacriacao = snapshotmei.compare_to(snapshotini,'lineno')
    #for stat in memoriacriacao[:3]:
        #print(stat)

    #memoriabusca = snapshotfin.compare_to(snapshotmei,'lineno')
    #for stat in memoriabusca[:3]:
        #print(stat)

    # mostra a memória
    mem = tracemalloc.get_traced_memory()
    #print('Memória: ',mem[1])


    # encerra o monitoramento
    tracemalloc.stop()

    del raizatual
    gc.collect()
    return tempofinal, resultado, mem[1]

# Algoritmo:

vetormemoria = []
vetortempo = []
vetorcomparacoes = []

for n in range(100):
    resultadofinal = buscaSequencial('cem.csv')
    vetortempo.append(resultadofinal[0])
    vetorcomparacoes.append(resultadofinal[1])
    vetormemoria.append(resultadofinal[2])

print('Média do tempo: ',statistics.mean(vetortempo))
print('Desvio padrão do tempo: ',statistics.stdev(vetortempo))

print('Média de comparações: ',statistics.mean(vetorcomparacoes))
print('Desvio padrão das comparações: ',statistics.stdev(vetorcomparacoes))

print('Média da memória: ',statistics.mean(vetormemoria))
print('Desvio padrão da memória: ',statistics.stdev(vetormemoria))

