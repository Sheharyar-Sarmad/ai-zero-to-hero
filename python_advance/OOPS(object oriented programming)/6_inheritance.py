
# Inheritance


# Inheritance is a mechanism where one class (child/subclass) acquires the properties and behaviors of another class (parent/superclass). It establishes an "is-a" relationship and enables code reuse, extensibility, and hierarchical classification.


# # Single Interitance

# class FactoryMumbai: # parent class / super class
#     a = 12
#     def hello(self):
#         print("\nhello this is a method mentioned inside the Factory class!\n")

# class FactoryPune(FactoryMumbai): # child class / sub class
#     pass
    
# obj = FactoryMumbai()
# obj2 = FactoryPune()

# obj2.hello()

# class Animal:
#     def __init__(self , name: str):
#         self.name = name
    
#     def show(self):
#         print(f"\nhello your name is {self.name}\n")
        
# class Human(Animal):
#     def __init__(self, name: str, age: int):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"\nhello your name is {self.name} , {self.age}\n")
    
# animal1 = Animal("Sheharyar")
# human1 = Human("Sarmad",12)

# human1.show() 
# animal1.show() 

# Multiple Inheritance(2 or more than 2 classes inherit by a class is called as multiple interitance based class)

# class Animal:
#     name1 = "lion"

# class Human:
#     name2 = "harsh"

# class Robots(Animal , Human):
#     name3 = "charli123"
    
# obj = Robots()
# print(f"\n{obj.name3}\n")
