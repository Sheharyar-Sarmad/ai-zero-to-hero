

# Abstraction

# Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object. It focuses on what an object does rather than how it does it, providing a simplified interface to the outside world.

# Example:

from abc import ABC , abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Square(abstract):
    def __init__(self , side):
        self.side = side

    def perimeter(self):
        print("i have created")
    
    def area(self):
        print("i have created this")
    
        
class Circle(abstract):
    def __init__(self , radius):
        self.radius = radius
        
    def perimeter(self):
        print("i have created")
    
    def area(self):
        print("i have created this")
        
obj = Square(7)
print(obj.side)
obj.perimeter()
obj.area()