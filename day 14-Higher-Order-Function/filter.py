# filter is a built-in higher order function

numbers= [1,2,3,4,5,6,7,8,9,10];

def is_even(num):
    if num%2==0:
        return True
    return False

def is_odd(num):
    if num%2!=0:
        return True
    return False

even= filter(is_even, numbers)
print(list(even))

odd= filter(is_odd, numbers) 
print(list(odd))

#lamba

evenLambda= filter(lambda num: num%2==0, numbers)
print("Lambda",list(evenLambda))

oddLambda= filter(lambda num: num%2!=0, numbers)
print("Lambda",list(oddLambda))