# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

evenTot=0
oddTot=0
for i in range(101):
    if(i%2==0):
        evenTot+=i
    elif(i%2==1):
        oddTot+=i

print(f"The sum of all evens is: {evenTot}. And the sum of all odds is{oddTot}.")