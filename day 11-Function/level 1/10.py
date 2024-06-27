# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(list):
    newList=[]
    for item in list:
        newList.append(item.capitalize())
    return newList

print(capitalize_list_items(["apple","banana"]))