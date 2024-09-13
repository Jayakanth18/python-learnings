# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age_set= set(age)
print(len(age)>len(age_set))
print(len(age)<len(age_set))
#2
# string- anything in single or double in python is considered as string.
# list- collection of items string,int or bool. ordered, changeable, allow duplicates.[]
# tuple- collection of items.all datatype can be included. ordered, changeable and allow duplicates values.()
#set- collection of items.unordered, unchangeable and didnt allow duplicate value.{}


#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence="I am a teacher and I love to inspire and teach people."
new_sentence= sentence.split()
unique_words= set(new_sentence)
unique_words_count= len(unique_words)
print(unique_words_count)

