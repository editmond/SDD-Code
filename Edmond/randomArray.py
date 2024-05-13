# generate random integer values
from numpy.random import seed
from numpy.random import randint
from datetime import datetime
def randomArray():
    # seed random number generator
    seed(None)
    # generate some integers
    values = randint(0, 10, 100)
    print(values)
    return values
