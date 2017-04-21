
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
        binElement = "{0:b}".format(intElement)
        binVector.append(binElement)

    return binVector
        

class Cromossomo:

    def __init__(self, genes):
        self.genes = genes
        self.fitness = fitness(genes)

def main():
    cromossomo = Cromossomo(intVectorToBinVector([1,1,1,1,1,1,1,1]))
    print(cromossomo.fitness)


if __name__ == '__main__':
    main()
