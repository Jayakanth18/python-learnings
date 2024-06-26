fruits = ['banana', 'orange', 'mango', 'lemon']
userInputFruit= str(input("enter the fruit: ")).lower()

if userInputFruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(userInputFruit)
    print(fruits)