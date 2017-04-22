import random

def crossover(pai1, pai2):
    corte = int(random.uniform(1,7))
    filho1 = []
    filho2 = []
    print corte
    for i in range(corte):
        filho1.append(pai1[i])
        filho2.append(pai2[i])

    print 'Filho 1' + str(filho1)
    print 'Filho 2' + str(filho2)
        
    for i in range(corte, len(pai2)):
        if(pai2[i] not in filho1):
            filho1.append(pai2[i])

    print 'Filho 1' + str(filho1)
    print 'Filho 2' + str(filho2)
            
    for i in range(corte):
        if(pai2[i] not in filho1):
            filho1.append(pai2[i])

    print 'Filho 1' + str(filho1)
    print 'Filho 2' + str(filho2)
    
    for i in range(corte, len(pai1)):
        if(pai1[i] not in filho2):
            filho2.append(pai1[i])

    print 'Filho 1' + str(filho1)
    print 'Filho 2' + str(filho2)
            
    for i in range(corte):
        if(pai1[i] not in filho2):
            filho2.append(pai1[i])

    print 'Filho 1' + str(filho1)
    print 'Filho 2' + str(filho2)

    return filho1,filho2

def crossover2(ind1, ind2):

    size = min(len(ind1), len(ind2))
    p1, p2 = [0]*size, [0]*size

    ind1 = binVectorToIntVector(ind1)
    ind2 = binVectorToIntVector(ind2)    
    
    #inicializa a posicao de cada individuos
    for i in xrange(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i
    #escolhe os pontos de crossover
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: #troca os pontos de crossover
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    
    #aplica o crossover entre os pontos de crossover
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
    temp = 0
    while(t1 == t2):
        t2 = int(random.uniform(1,7))
    temp = gene[t2]
    gene[t2] = gene[t1]
    gene[t1] = temp
    return gene

def main():
    pai1 = [1,2,3,4,5,6,7,8]
    pai2 = [3,7,8,2,6,5,1,4]

    print 'Pai 1' + str(pai1)
    print 'Pai 2' + str(pai2)
    filho1, filho2 = crossover(pai1,pai2)
  
    

    
    
if __name__ == "__main__":
    main();
