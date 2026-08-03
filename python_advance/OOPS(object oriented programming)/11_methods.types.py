
# Python has three main types of methods in object-oriented programming, each serving a different purpose and having different access to class and instance data.

# 1. Instance Methods

# Characteristics:

# Most common type of method
# Takes self as first parameter
# Can access and modify instance attributes
# Can access class attributes via self.__class__ or ClassName
# Called on instances of the class

# 2. Class Methods

# Characteristics:

# Takes cls as first parameter (refers to the class itself)
# Decorated with @classmethod
# Can access and modify class attributes
# Cannot access instance attributes (no self)
# Can be called on class or instance
# Used for factory methods and class-level operations

# 3. Static Methods

# Characteristics:
    
# No self or cls parameter
# Decorated with @staticmethod
# Cannot access class or instance attributes directly
# Acts like a regular function but belongs to class namespace
# Called on class or instance
# Used for utility functions related to the class

class Animal:
    name = "lion" # Class Attribute
    
    def __init__(self , age): # instance method
        self.age = age # instance attribute
    
    def show(self): # instance method
        print(f"The age is {self.age}")
    
    @classmethod # class method 
    def hello(cls):
        print(cls.name)
    
    @staticmethod
    def static():
        print("kiase ho")
        
obj = Animal(12)
obj.hello()
obj.show()