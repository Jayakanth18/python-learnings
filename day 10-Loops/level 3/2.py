# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits=['banana', 'orange', 'mango', 'lemon',"apple", "pineapple"];
rev=[]

for i in range(len(fruits)-1,-1,-1):
    rev.append(fruits[i])

print(fruits)
print(rev)

# range(len(fruits) - 1, -1, -1) generates a sequence of indices from the last index (len(fruits) - 1) to 0.