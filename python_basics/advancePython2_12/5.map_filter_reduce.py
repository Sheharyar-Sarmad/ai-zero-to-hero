

# Map example
l = [12 , 11 , 10 , 9 , 8 , 7 , 6, 5 ,4 , 3, 2]

cube = lambda x: x**3

cubeList = map(cube , l)
cubeList = list(cubeList)
print(cubeList , type(cubeList))

# Filter example:

def even(n) :
    if n%2 == 0 :
        return True
    else :
        return False


def odd(n) :
    if n%2 != 0 :
        return True
    else :
        return False

onlyEven = filter(even , l) 
onlyOdd = filter(odd , l) 
print(list(onlyEven))
print(list(onlyOdd))


# Reduce Example:

# WE HAVE TO IMPORT REDUCE FROM FUNCTOOLS
 
from functools import reduce

sumofnums = lambda a , b : a + b
mulofnums = lambda x,y : x*y

reduceOfsum = reduce(sumofnums , l)
reduceOfMul = reduce(mulofnums , l)

print(reduceOfsum)
print(reduceOfMul)