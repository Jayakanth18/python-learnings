# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(list:list):
    list_copy=list.copy();
    random.shuffle(list_copy)
    return list_copy

dummy_list = [1, 2, 3, 4, 5]

print(shuffle_list(dummy_list))
