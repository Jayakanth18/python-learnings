# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(list, item):
    list.append(item)
    return list

fruits=["apple","pine apple","banana","cherry","pomeogranate","jack fruit"]
numbers=[2,4,6,8,10]
print(add_item(fruits,"mango"))
print(add_item(numbers,12))