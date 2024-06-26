# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

mark=int(input("Enter the mark: "));

if mark<100 and mark>=80:
    print("A")
elif mark>=70 and mark<=79:
    print("B")
elif mark>=60 and mark<=69:
    print("C")
elif mark>=50 and mark<=59:
    print("D");
else:
    print("F")