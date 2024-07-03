# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

from random import *

def rand_num():
    return sample(range(10),7)

print(rand_num())
