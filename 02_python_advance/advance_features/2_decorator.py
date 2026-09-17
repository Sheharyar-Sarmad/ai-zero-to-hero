

# # 📖 What is a Decorator?
# A decorator is a function that takes another function as an argument, adds extra functionality to it, and returns a new function.

# Think of it as wrapping one function with another to extend its behavior.

# 🔑 Simple Definition
# A decorator is a function that modifies the behavior of another function without changing its source code.

# Example

# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
        
# obj = Animal()
# obj.show # this will properly becuase it contain @property decorater which didnt need parenthesis to call the function


def decorate(func):
    def wrapper():
        print("i will print myself before the function")
        func()
        print("i wll print myself after the function")
    
    return wrapper
        
@decorate
def hello():
    print("hello i am sheharyar sarmad")
    
hello()

# Real code

l = [3,4,7,5,8]

for i,v in enumerate(l) :
    if v == 5 :
        print(f'index: {i} , values: {v}')

# Pseudo code

# Set l(list) = [3,4,7,5,8]

# go for index and value one by one in enumerate(this will give both index and value) 
# l(apply loop on this list): 
     # if any value of a list == 5 :
        #  then print on output in an f string that index of that value is {i}(means that index value in which i appears) and value is {v}(exact 5 value as an int)
