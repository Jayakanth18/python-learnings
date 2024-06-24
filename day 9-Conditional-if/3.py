# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))

if a>b:
    print(a,"greater then",b)
elif a==b:
    print(a,"equals to",b)
else:
    print(a,"lesser than",b)