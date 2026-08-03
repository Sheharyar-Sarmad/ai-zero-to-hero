
# Class attributes are variables that belong to the class itself, not to instances of the class. They are shared across all instances.

# Instance attributes are variables that belong to a specific instance (object) of a class. Each object has its own copy of these attributes, and changes to one instance don't affect others.


class Animal:
    name = "lion" # Class Attribute
    
    def __init__(self , color):
        self.color = color
    
    