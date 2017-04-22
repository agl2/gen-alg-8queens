import itertools
import random
from numpy import *
import Gnuplot

def main():
    #set = [0,1,2,3,4,5,6,7]
    #resultado = list(itertools.permutations(set,8))
    #final = random.sample(resultado,10000)
    #print (final)

    gplt = Gnuplot.Gnuplot(debug=1)

    gplt.reset()
    x=[2,4,8,16,32,64]
    d = Gnuplot.Data(x, title='calculated by python')
    gplt('set data style lines')
    gplt.xlabel('Input')
    gplt.ylabel('Output')
    gplt.plot(d)
    raw_input('Please press return to continue...\n')

    
if __name__ == "__main__":
    main()


