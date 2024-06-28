# Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(parameter):
    if len(parameter) == 0:
     return True
    else:
       return False
    
print(is_empty("dd"))
print(is_empty([]))
print(is_empty({})) 