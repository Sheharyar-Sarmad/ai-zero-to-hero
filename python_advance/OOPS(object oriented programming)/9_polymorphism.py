

# Polymorphism:

# Polymorphism (meaning "many forms") is the ability of objects of different classes to respond to the same method call in their own specific way. It allows one interface to be used for a general class of actions, with the specific action determined by the actual object type at runtime.


# There are two method of polymorphism in python even tough more programming languages have 3 methods "method overloading"

# Example of over-riding() 
# impotant concept that overriding feature always works with inheritance 

# class Animal:
#     def show(self) :
#         print("hello i am Sheharyar")
        
# class Human(Animal):
#     def show(self):
#         print("how are you")
        
# obj = Human()
# obj.show() # how are you will print becuase the obj is Human class and it over ride the Animal class show() function

# Second Example:

class Animal:
    def show(self):
        print("\nI am showing")

class Human:
    def show(self):
        print("hello I am also showing\n")
        
obj = Animal()
obj2 = Human()

obj.show()
obj2.show()