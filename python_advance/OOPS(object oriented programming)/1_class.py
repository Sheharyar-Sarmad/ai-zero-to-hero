
# A class is a blueprint or template for creating objects. It defines the data (attributes) and functions (methods) that the objects created from it will have.

class Factory :
    # There are two types of things in class attributes and methods
    a = 12 # attribute
    
    def hello(self) : # method
        print('Hello how are you!')
        
    print("hello how are you i am getting initialized!")
    
print(Factory().a)
Factory().hello()