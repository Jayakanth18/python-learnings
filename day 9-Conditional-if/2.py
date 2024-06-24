# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

age=30;
myAge=int(input("Enter your age:"))
diff= 30-myAge

if(age>myAge):
    print("you are",diff,"years younger then me")
elif age==myAge:
    print("same age")
else:
    print("you are",diff,"older then me")