# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero=  [x for x in numbers if x<=0]

print(negative_and_zero)