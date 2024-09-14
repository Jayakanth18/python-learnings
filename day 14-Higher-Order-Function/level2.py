from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1.Use map to create a new list by changing each country to uppercase in the countries list
countriesInCaps= list(map(lambda country:country.upper(), countries))
print(countriesInCaps)

#2.Use map to create a new list by changing each number to its square in the numbers list
squareNumbers= list(map(lambda num: num**2, numbers))
print(squareNumbers)

#3.Use map to change each name to uppercase in the names list
upperNames= map(lambda name: name.upper(), names)
print(list(upperNames))

#4.Use filter to filter out countries containing 'land'.
countriesWithLand= filter(lambda country:"land" not in country, countries)
print(list(countriesWithLand))

#5.Use filter to filter out countries having exactly six characters.
newCountries= list(filter(lambda country: len(country) != 6, countries))
print(newCountries)

#6.Use filter to filter out countries containing six letters and more in the country list.
countriesWithin6Letters= list(filter(lambda country: len(country)<=6, countries))
print(countriesWithin6Letters)

#7.Use filter to filter out countries starting with an 'E'
countriesStartingInE= list(filter(lambda country: country[0] != "E", countries))
print(countriesStartingInE)

#8.Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
evenSquare= map(lambda num: num**2,filter(lambda num: num%2==0, numbers))
print(list(evenSquare))

#9.Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

#gpt answer
def get_string_lists(lst):
    # Use list comprehension to filter out only string items
    return [item for item in lst if isinstance(item, str)]

# Example usage:
input_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
string_list = get_string_lists(input_list)
print(string_list)

#10. Use reduce to sum all the numbers in the numbers list.
sumOfNumbers= reduce(lambda x,y: x+y, numbers)
print(sumOfNumbers)

#11.Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

