import itertools
import random

def main():
    set = [0,1,2,3,4,5,6,7]
    resultado = list(itertools.permutations(set,8))
    final = random.sample(resultado,10000)
    print (final)
    
if __name__ == "__main__":
    main();


