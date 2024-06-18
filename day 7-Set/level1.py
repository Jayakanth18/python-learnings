# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
#2
it_companies.add("Twitter")
# print(it_companies)

#3
more_it_companies= {"Zoho", "Freshworks", "TCS", "HCL"}
it_companies.update(more_it_companies)
print(it_companies)

#4
it_companies.remove("Oracle")
print(it_companies)

#5

# both remove and discard used to remove a item from set but if the item is not available in set remove() method will throw a error but discard() method didn't.

