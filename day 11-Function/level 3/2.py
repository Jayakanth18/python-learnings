# Write a functions which checks if all items are unique in the list


def is_unique(list:list):
    newSet=set(list)
    return len(list) == len(newSet)

print(is_unique([1,2,3,5,7,8,9,1]))
print(is_unique([1,2,3,5,7,8,9]))