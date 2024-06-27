# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total=0
    for num in nums:
        total +=num
    return total

print(add_all_nums(13,57))
print(add_all_nums(-30,40,-10))
print(add_all_nums(15,90,5,-90,10))