#1
dog={}
# dog=dict()

#2
dog["color"]= "brown"
dog["breed"]=  "german shepherd"
dog["age"]= 2
# print(dog["age"])

#3
student={
    "first_name": "Jayakanth",
    "last_name": "R",
    "gender": "Male",
    "age": 23,
    "marital status": "Single",
    "skills":["Photography","Programming","Editing"],
    "country": "India",
    "city": "Thiruvallur",
    "address": "1/43 Athigathur"
}
# print(student["skills"][1])

#4
print(len(student))

#5
skill=student["skills"]
print(type(skill)) #true

#6
student["skills"].append("Logical Thinking")
student["skills"].append("Quick Learner")
print(student["skills"])

#7
keyList= student.keys()
print(keyList)
# print(type(keyList))

#8
student.values()

#9
student_tuple=student.items()
print(student_tuple)
# print(type(student_tuple))

#10
student.pop("marital status")
# print(student)

#11
del student;
# print(student)