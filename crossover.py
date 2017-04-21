import random

def crossover(pai1, pai2):
    corte = int(random.uniform(1,7))
    filho1 = []
    filho2 = []
    print (corte)
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
    filho1, filho2 = crossover(pai1,pai2)
    print (filho1)
    print (filho2)
    
    filho1 = mutacao(filho2)
    print (filho2)
    

    
    
if __name__ == "__main__":
    main();
