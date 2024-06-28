# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def sum_of_even(n):
    sum=0
    for i in range(n):
        if(i%2==0):
            sum +=i
    return sum


print(sum_of_even(5))