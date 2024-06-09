age= 23;
height= 5.8;
complex= 1 + 1j;

#4
base= input('Enter the base of the triangle: ');
height= input('Enter the height of the triangle: ');
area_of_triangle= 0.5*float(base)*float(height);
print('Area of the triangle:', area_of_triangle);

#5
sideA= int(input("enter value of side A: "))
sideB= int(input("enter value of side B: "))
sidec= int(input("enter value of side C: "))
perimeter_of_triangle= sideA+sideB+sidec
print("The perimeter of the triangle is:",perimeter_of_triangle)

#6
length= int(input("enter length:"))
width= int(input("enter width:"))
areaOfRectangle= length*width
perimeterOfRectangle= 2*(length+width)
print(areaOfRectangle, perimeterOfRectangle)

#7
radius= int(input("radius of the circle: "))
area_of_circle= 3.14*radius*radius
circumference_pf_circle= 2*3.14*radius
print(area_of_circle, round(circumference_pf_circle)) #round used to round off the value

#12
print(len("pyrhon") > len("dragon"))

#13 
print("on" in "python")
print("on" in "dragon")

# 14
print("jargon" in "I hope this course is not full of jargon")

# 15
print("on" not in "python" and "on" not in "dragon")

#16
inputText= "python"
length= len(inputText)
floatValue= float(length)
print(type(str(floatValue)))

#17
# if the remainder is not zero its is odd number.

#19
print(type(10) == type("10"))

#21
hours= int(input("enter the hours: "))
rate= int(input("enter rate per hour: "))
print("ypur weekly earnings is:", hours*rate)

#22
years_of_life= int(input("enter number of years you lived:"))
seconds= 60*60*24*365
print("You have lived for", years_of_life*seconds, "seconds")



