# -*- coding: cp1252 -*-
import random
import itertools
import Gnuplot
import copy
import numpy as np

#FITNESS_TYPE = 1 #fitness = choques
FITNESS_TYPE = 2  #fitness = 1/(1+choques)


class Cromossomo:

    def __init__(self, genes, pai1, pai2, geracao, gerador):
        self.genes = genes
        self.fitness = fitness(genes)
        self.pai1 = pai1
        self.pai2 = pai2
        self.geracao = geracao
        self.gerador = gerador
    def __copy__(self):
        return Cromossomo(self.genes, None, None, self.geracao, self.gerador)
    def __deepcopy__(self, memo):
        return Cromossomo(self.genes, copy.copy(self.pai1), copy.copy(self.pai2), self.geracao, self.gerador)
		
		
def crossover(pai1, pai2):
    corte = int(random.uniform(1,6))
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
    gene_novo = []
    gene_novo += gene
#    print('t1 ='+ repr(t1))
#    print('t2 ='+ repr(t2))
    temp = 0
    while(t1 == t2):
        t2 = int(random.uniform(1,7))
    temp = gene_novo[t2]
    gene_novo[t2] = gene_novo[t1]
    gene_novo[t1] = temp
    return gene_novo

    
#usar permutions se for para apenas permutacoes e product se for para todas as combinacoes possiveis
#se usar product a funcao de fitness deve ser outra para considerar tambem a colisao nas linhas
def iniciar_populacao():
    set = [0,1,2,3,4,5,6,7]
    resultado = list(itertools.permutations(set,8))
    final = random.sample(resultado,100)
    for i in range(len(final)):
        final[i] = Cromossomo(intVectorToBinVector(final[i]), None, None, 0, 'I')
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
    if FITNESS_TYPE == 1:
        return clashes
    else:
        return float(1)/(1 + clashes)

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

def mostrarMelhorIndividuo(melhorIndividuo):
    print '\n\nMelhor individuo:'
    print 'Genes: ' +  str(binVectorToIntVector(melhorIndividuo.genes))
    print 'Fitness ' +  str(melhorIndividuo.fitness)
    print 'Gerador ' +  str(melhorIndividuo.gerador)
    print 'Geracao ' +  str(melhorIndividuo.geracao)
    pai1 = melhorIndividuo.pai1
    pai2 = melhorIndividuo.pai2
    print 'Pai1: '
    if(pai1 is not None):
        print '\tGenes ' + str(binVectorToIntVector(pai1.genes))
        print '\tFitness ' +  str(pai1.fitness)
        print '\tGerador ' +  str(pai1.gerador)
        print '\tGeracao ' +  str(pai1.geracao)
    else:
        print '\tNone'

    print 'Pai2: '
    if(pai2 is not None):
        print '\tGenes ' + str(binVectorToIntVector(pai2.genes))
        print '\tFitness ' +  str(pai2.fitness)
        print '\tGerador ' +  str(pai2.gerador)
        print '\tGeracao ' +  str(pai2.geracao)
    else:
        print '\tNone'
    

def main():
    
    filho1 = []
    filho2 = []
    i = 0

    #inicia a populacao com 100 individuos e os ordena de acordo com o fitness
    populacao = iniciar_populacao()
    #ordena os pais de acordo com o fitness
    if FITNESS_TYPE == 1:
        populacao.sort(key=lambda p : p.fitness)
    else:
        populacao.sort(key=lambda p : p.fitness, reverse=True)


    media = []
    maximo = []
    minimo = []
    variancia = []
    melhorIndSalvo = False
    
    #a partir daqui tem que ser feito o laco para poder tentar encontrar a solucao para o problema
    while(i <= 10000):
    
        #seleciona 5 pais de forma aleatoria
        pais = random.sample(populacao, 5)
        
        if FITNESS_TYPE == 1:
            pais.sort(key=lambda p : p.fitness)
        else:
            pais.sort(key=lambda p : p.fitness, reverse=True)
        
        #pega os dois com melhor fitness para fazer o crossover
#        print(pais[0].genes)
#        print(pais[1].genes)
        
        pai1 = pais[0]  
        pai2 = pais[1]

        filho1 = None
        filho2 = None
		
	#random.uniform(0,1) <= 0.9
        if(random.uniform(0,1) <= 0.9):
            genes1, genes2 = crossover(pai1.genes,pai2.genes)
            filho1 = Cromossomo(genes1, pai1, pai2, i+1, 'C')
            filho2 = Cromossomo(genes2, pai1, pai2, i+1, 'C')
        
           
        #para mutacao seria
        #     random.uniform(0,1) <= 0.4
        if(random.uniform(0,1) <= 0.4):
            if(filho1 is not None):
                filho1.genes = mutacao(filho1.genes)
                filho1.fitness = fitness(filho1.genes)
                filho1.gerador = 'B'
            else:
                filho1 = Cromossomo(pai1.genes, pai1, None, i+1, 'M')
                
        #para mutacao seria
        #     random.uniform(0,1) <= 0.4
        if(random.uniform(0,1) <= 0.4):
            if(filho2 is not None):
                filho2.genes = mutacao(filho2.genes)
                filho2.fitness = fitness(filho2.genes)
                filho2.gerador = 'B'
            else:
                filho2 = Cromossomo(pai2.genes, pai2, None, i+1, 'M')

                

        if(filho1 is not None and filho2 is not None):
            #os filhos sao inseridos na populacao
            populacao.append(filho1)
            populacao.append(filho2)
            #ordena a populacao pelo fitness para poder excluir os piores
            if FITNESS_TYPE == 1:
                populacao.sort(key=lambda p : p.fitness)
            else:
                populacao.sort(key=lambda p : p.fitness, reverse=True)

            populacao.pop()
            populacao.pop()

        soma = 0
        for ind in populacao:
           soma += ind.fitness
        media.append(soma/len(populacao))
        variancia.append(np.var(media[i]))

        if FITNESS_TYPE == 1:
            minimo.append(populacao[0].fitness)
            maximo.append(populacao[-1].fitness)
        else:
            maximo.append(populacao[0].fitness)
            minimo.append(populacao[-1].fitness)

        print 'Iteracao ' + str(i) + ' fitness max:' + str(maximo[i]) + ' fitness min:' + str(minimo[i])

        if FITNESS_TYPE == 1:
            if(populacao[0].fitness == 0 and not melhorIndSalvo):
                melhorIndividuo = copy.deepcopy(populacao[0])
                melhorIndSalvo = True
            if(populacao[-1].fitness == 0):
                break
        else:
            if(populacao[0].fitness == 1 and not melhorIndSalvo):
                melhorIndividuo = copy.deepcopy(populacao[0])
                melhorIndSalvo = True
            if(populacao[-1].fitness == 1):
                break
        i += 1
    #End While

    mostrarMelhorIndividuo(melhorIndividuo)
    gplt = Gnuplot.Gnuplot(debug=1)

    gplt.reset()
    mediaData = Gnuplot.Data(media, title='Fitness M�dio')
    minData = Gnuplot.Data(minimo, title='Fitness M�nimo')
    maxData = Gnuplot.Data(maximo, title='Fitness M�ximo')
    gplt('set data style lines')
    gplt.xlabel('Iteracao')
    gplt.ylabel('Fitness')
    if FITNESS_TYPE == 2:
        gplt('set yrange [0:1.5]')
        
    gplt.plot(maxData, mediaData, minData)
    raw_input('Please press return to continue...\n')

    gplt.reset()
    varianciaData = Gnuplot.Data(variancia, title='Variancia')
    gplt('set data style lines')
    gplt.xlabel('Iteracao')
    gplt.ylabel('Vari�ncia Fitness M�dio')
        
    gplt.plot(varianciaData)
    raw_input('Please press return to continue...\n')

if __name__ == '__main__':
    main()
