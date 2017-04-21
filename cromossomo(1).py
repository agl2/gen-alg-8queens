import random
import itertools


class Cromossomo:

    def __init__(self, genes):
        self.genes = genes
        self.fitness = fitness(genes)

def crossover(pai1, pai2):
    corte = int(random.uniform(1,7))
    filho1 = []
    filho2 = []
#    print (corte+1)
    for i in range(corte):
        filho1.append(pai1[i])
        filho2.append(pai2[i])
        
        
    for i in range(corte, len(pai2)):
        if(pai2[i] not in filho1):
            filho1.append(pai2[i])
            
    for i in range(corte):
        if(pai2[i] not in filho1):
            filho1.append(pai2[i])
    
    for i in range(corte, len(pai1)):
        if(pai1[i] not in filho2):
            filho2.append(pai1[i])
            
    for i in range(corte):
        if(pai1[i] not in filho2):
            filho2.append(pai1[i])

    return filho1,filho2

    
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
    
        filho1 = pais[0]
        filho2 = pais[1]    
        
        
        #nao sei se ta certo usar essa funcao para delimitar a probabilidade de ocorre um crossover
        #     random.uniform(0,1) <= 0.9
        if(random.uniform(0,1) <= 0.9):
            filho1.genes, filho2.genes = crossover(filho1.genes,filho2.genes)
           
        #para mutacao seria
        #     random.uniform(0,1) <= 0.4
        if(random.uniform(0,1) <= 0.4):
            filho1.genes = mutacao(filho1.genes)
            filho2.genes = mutacao(filho2.genes)
            

        
        #os filhos sao inseridos na populacao
        populacao.append(filho1)
        populacao.append(filho2)
        
        
        #ordena a populacao pelo fitness para poder excluir os piores
        populacao.sort(key=lambda p : p.fitness)
        populacao.pop()
        populacao.pop()
        if(populacao[0].fitness == 0):
            print(populacao[0].genes)
            print(populacao[0].fitness)
            print (i)
            break
        i += 1
    print(i)
    print(populacao[0].genes)
    print(populacao[0].fitness)
    
    


if __name__ == '__main__':
    main()
