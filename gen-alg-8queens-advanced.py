import random
import itertools


class Cromossomo:

    def __init__(self, genes):
        self.genes = genes
        self.fitness = fitness(genes)

def crossover(ind1, ind2):

    size = min(len(ind1), len(ind2))
    p1, p2 = [0]*size, [0]*size

    ind1 = binVectorToIntVector(ind1)
    ind2 = binVectorToIntVector(ind2)    
    
    for i in xrange(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i
    
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: 
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    

    for i in xrange(cxpoint1, cxpoint2):

        temp1 = ind1[i]
        temp2 = ind2[i]

        ind1[i], ind1[p1[temp2]] = temp2, temp1
        ind2[i], ind2[p2[temp1]] = temp1, temp2
        
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
    
    ind1 = intVectorToBinVector(ind1)
    ind2 = intVectorToBinVector(ind2)      
    
    return ind1, ind2

    
def mutacao(gene):
    t1 = int(random.uniform(1,7))
    t2 = int(random.uniform(1,7))
#    print('t1 ='+ repr(t1))
#    print('t2 ='+ repr(t2))
    temp = 0
    while(t1 == t2):
        t2 = int(random.uniform(1,7))
    temp = gene[t2]
    gene[t2] = gene[t1]
    gene[t1] = temp
    return gene

    
#usar permutions se for para apenas permutacoes e product se for para todas as combinacoes possiveis
#se usar product a funcao de fitness deve ser outra para considerar tambem a colisao nas linhas
def iniciar_populacao():
    set = [0,1,2,3,4,5,6,7]
    resultado = list(itertools.permutations(set,8))
    final = random.sample(resultado,100)
    for i in range(len(final)):
        final[i] = Cromossomo(intVectorToBinVector(final[i]))
    return final


def fitness(genes):
    clashes = 0
    for i in range(len(genes)):
        gene1_int = int(genes[i], 2)
        for j in range(len(genes)):
            gene2_int = int(genes[j], 2)
            if(i != j):
                dx = abs(i - j)
                dy = abs(gene1_int - gene2_int)
                if(dx == dy):
                    clashes += 1
        #endFor
    #endFor
    return clashes

def intVectorToBinVector(intVector):
    binVector = []
    for intElement in intVector:
        binElement = "{0:03b}".format(intElement)
        binVector.append(binElement)

    return binVector

def binVectorToIntVector(binVector):
    intVector = []
    for binElement in binVector:
        intElement = int(binElement, 2)
        intVector.append(intElement)

    return intVector


def main():
    
    filho1 = []
    filho2 = []
    i = 0

    #inicia a populacao com 100 individuos e os ordena de acordo com o fitness
    populacao = iniciar_populacao()      
    populacao.sort(key=lambda p : p.fitness)
    
    #a partir daqui tem que ser feito o laco para poder tentar encontrar a solucao para o problema
    
    while(i <= 10000):
    
        #seleciona 5 pais de forma aleatoria
        pais = random.sample(populacao, 5)
        
        #ordena os pais de acordo com o fitness
        pais.sort(key=lambda p : p.fitness)
        
        #pega os dois com melhor fitness para fazer o crossover
#        print(pais[0].genes)
#        print(pais[1].genes)
        
        #nao sei se ta certo usar essa funcao para delimitar a probabilidade de ocorre um crossover
        #     random.uniform(0,1) <= 0.9

        
        genes1 = []
        genes2 = []
        if(random.uniform(0,1) <= 0.9):
            genes1, genes2 = crossover(pais[0].genes,pais[1].genes)
        
           
        #para mutacao seria
        #     random.uniform(0,1) <= 0.4
        if(random.uniform(0,1) <= 0.1):
            if(genes1 != [] and genes2 != []):
                genes1 = mutacao(genes1)
                genes2 = mutacao(genes2)
            else:
                genes1 = mutacao(pais[0].genes)
                genes2 = mutacao(pais[1].genes)
                

        if(genes1 != [] and genes2 != []):
            filho1 = Cromossomo(genes1)
            filho2 = Cromossomo(genes2)
            #os filhos sao inseridos na populacao
            populacao.append(filho1)
            populacao.append(filho2)
            #ordena a populacao pelo fitness para poder excluir os piores
            populacao.sort(key=lambda p : p.fitness)
            populacao.pop()
            populacao.pop()

        print '\n\nIteracao ' + str(i)
        print 'Melhor fitness ' +  str(populacao[0].fitness)
        for ind in populacao[0:5]:
            print 'Individuo: ' + str(binVectorToIntVector(ind.genes))
            print 'Fitness: ' + str(ind.fitness)
        if(populacao[0].fitness == 0):
            break
        i += 1
    #End While


if __name__ == '__main__':
    main()

