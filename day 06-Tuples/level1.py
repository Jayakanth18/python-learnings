#1
empty_tuple= tuple()
print(type(empty_tuple))

#2
myBrothers= ("Hari Haran", "Jayasureya", "Karthick");
mySisters= ("Gomathi", "Lavanya", "Sangeetha");
#3
my_sibilings= myBrothers+mySisters
#4
print("total no of sibilings:",len(my_sibilings))
#5
temp_list=list(my_sibilings)
temp_list.append("Kalyani")
temp_list.append("Ramadoss")
my_family=tuple(temp_list)
# print(my_family)

# level 2 -1

(*sibilings,mother,father)= my_family
print(sibilings,mother,father)