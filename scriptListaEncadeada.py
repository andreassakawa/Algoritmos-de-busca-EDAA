import random
import csv
import time
import tracemalloc
import statistics
import gc

# código utilizado para gerar vetores com número de 1 a n
#vetor = list(range(1,101,1))

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
        self.prox = None

# define classe Lista e suas funções
class ListaEnc:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, x):
        novo = No(x)
        if self.head is None:
            self.head = novo
            return
        else:
            novo.prox = self.head
            self.head = novo

    def searchByData(self, x):
        atual = self.head
        comparacoes = 0
 
        comparacoes += 1
        if atual.valor == x:
            #print('Valor encontrado!')
            return comparacoes
    
        while atual is not None and atual.prox.valor != x:
            comparacoes += 1
            atual = atual.prox
    
        comparacoes += 1
        if atual is None:
            #print('Valor não encontrado!')
            return comparacoes
        else:
            #print('Valor encontrado!')
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

    # cria objeto do tipo Lista
    lista = ListaEnc()

    # código para ler os valores do arquivo CSV e preencher a lista
    with open(nomearquivo, 'r') as arquivocsv:
        leitor = csv.reader(arquivocsv)
        for linha in leitor:
            for indice in linha:
                lista.insertAtBegin(int(indice))
            entrada = int(random.choice(linha))

    #snapshotmei = tracemalloc.take_snapshot()

    # define valor a ser buscado
    #entrada = 44942

    # código que salva o tempo inicial
    tempoinicial = time.time()

    resultado = lista.searchByData(entrada)

    # imprime a diferença entre o tempo atual e o inicial
    #print("Tempo busca binária: %s segundos" % (time.time()-tempoinicial))
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

    del lista
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

