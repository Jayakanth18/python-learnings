# map is a built-in higher order function

numbers=[1,2,3,4,5,6];

def square(num):
    return num**2

numbers_squared= map(square,numbers);

print(list(numbers_squared))

# with lambda function

numbers_squared_lambda= map(lambda num: num**2, numbers)
print(list(numbers_squared_lambda))


#example 2
string_nums= ['1', '2', '3', '4', '5'];

int_nums= map(int, string_nums)
print(string_nums, list(int_nums))


#example 3
userNames= ['ashwin', 'bharath', 'chris', 'dinesh', 'eshwar'];

def nameToUpper(name:str):
    return name.upper()

upperNames= map(nameToUpper, userNames)
print(list(upperNames))

#with lambda

upperNamesLambda= map(lambda name: name.upper(), userNames)
print(list(upperNamesLambda))