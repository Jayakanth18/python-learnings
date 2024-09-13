#A function can take one or more functions as parameters
#A function can be returned as a result of another function

#from geeksforgeeks

# 1.function passed as a argument to another function.
def shout(text:str):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(function):
    greeting= function("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)

# 2. function returning another function

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15= create_adder(15)
print(add_15(10))