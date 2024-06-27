# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


def sum_all_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

print(sum_all_numbers(5))
print(sum_all_numbers(10))
print(sum_all_numbers(100))