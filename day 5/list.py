#1
empty_list= list()
# print(type(empty_list))

#2
fruits= ["apple", "chikku", "orange", "mango", "jack fruit"]

#3
print(len(fruits))

#4
print(fruits[0])
print(fruits[len(fruits)//2])
print(fruits[-1])

#5
mixed_data_types= ["jayakanth", 23, 5.8, "single", "thiruvallur"]

#6
it_companies= ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"];

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

#10
it_companies[0]= "Zoho"
print(it_companies)

#11
it_companies.insert(0,"TCS")
print(it_companies)

#12
it_companies[len(it_companies)//2]= "HCL"

#13
it_companies[-1]= it_companies[-1].upper()
print(it_companies)

#14
it_companies.append("#;")
print(it_companies)

#15
print("HCL" in it_companies)

#16
it_companies.sort(reverse=False)
print(it_companies)

#17
it_companies.sort(reverse=True)
print(it_companies)

#18
print(it_companies[3:])
#19
print(it_companies[:-3])

#21
print(it_companies.pop(0))
#22
print(it_companies.pop(len(it_companies)//2))
#23
print(it_companies.pop())
#24
it_companies=[]
print(it_companies)
#25
del it_companies

#26,27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack= front_end+back_end
print(full_stack)