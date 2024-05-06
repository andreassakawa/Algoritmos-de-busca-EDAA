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

# Função que realiza a busca sequencial dentro de um vetor. 
# - Recebe:(vetor a ser buscado, valor a ser encontrado)
def sequencialSearch(vet, x):
        comparacoes = 0
        comparacoes += 1
        if x in vet:
            for indice in vet:
                comparacoes +=1
                if x == indice:
                    #print('Valor encontrado!')
                    return comparacoes
        else:
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

    vetor = []

    # código para ler os valores do arquivo CSV e preencher o vetor
    with open(nomearquivo, 'r') as arquivocsv:
        leitor = csv.reader(arquivocsv)
        for linha in leitor:
            for x in range(0,len(linha)):
                vetor.append(int(linha[x]))

    #snapshotmei = tracemalloc.take_snapshot()

    # define valor a ser buscado
    entrada = random.choice(vetor)
    #entrada = 15952

    # código que salva o tempo inicial
    tempoinicial = time.time()

    # Busca Sequencial
    resultado = sequencialSearch(vetor, entrada)

    tempofinal = time.time() - tempoinicial
    # imprime a diferença entre o tempo atual e o inicial
    #print("Tempo busca sequencial: %s segundos" % (time.time()-tempoinicial))

    # imprime o número de comparações realizadas
    #print("Número de comparações: ",resultado)

    #snapshotfin = tracemalloc.take_snapshot()

    #memoriacriacao = snapshotmei.compare_to(snapshotini,'lineno')
    #for stat in memoriacriacao[:3]:
        #print(stat)

    #memoriabusca = snapshotfin.compare_to(snapshotmei,'lineno')
    #for stat in memoriabusca[:3]:
        #print(stat)

    mem = tracemalloc.get_traced_memory()
    #print('Memória: ',mem[1])

    # encerra o monitoramento
    tracemalloc.stop()

    del vetor
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

