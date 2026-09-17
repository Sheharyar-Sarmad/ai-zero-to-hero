
class Employee:
    def __init__(self) :
        print(f'Contructor of the Employee...')
    a = 1

class Programmer(Employee):
    def __init__(self) :
        print(f'Contructor of the Programmer...')
    def hh(self) :
        print("Hello hhh...")
    b = 2

class Manager(Programmer) :
    def __init__(self) :
        super().__init__()
        super().hh()
        print(f'Contructor of the Manager...')
    c = 3

o =  Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows the error as there is no attribute(instance , class) in Employee class

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)