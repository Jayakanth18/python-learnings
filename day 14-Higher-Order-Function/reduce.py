# reduce is a built-in higher order function in python
from functools import reduce

numbers= [1,2,3,4,5,6,7,8,9,10];

def total(x,y):
    return int(x)+int(y)

numTotal= reduce(total, numbers)
print(numTotal)

#lambda
totalLambda= reduce(lambda x,y: int(x)+int(y), numbers)
print(totalLambda)