# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))
diff=18-age;
if age>=18:
    print("You are old enough to learn to driving")
else:
    print("You need",diff,"more years to learn driving")