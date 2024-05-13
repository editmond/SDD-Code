from numpy.random import seed
from numpy.random import randint

def randomSearchValue():
    seed()
    searchValue = randint(low=0, high=10)
    return searchValue
