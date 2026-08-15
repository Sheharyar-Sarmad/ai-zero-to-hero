

# from typing import Literal

# class Person:
#     def __init__(self, name: str, age: int, gender: str = Literal['Male', 'Female'], profession: str = None):
#         self.name = name 
#         self.age = age
#         self.gender = gender
#         self.profession = profession

#     def greet(self):
#         return f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.profession}."

#     def __del__(self):
#         print(f"{self.name} has been deleted.")

# p = Person("John", 30, "Male", "Engineer")
# print(p.greet())
# del p 


class Vector: 
    def __init__(self, x , y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        return 10

    def __call__(self):
        print("Hello! I was called!")

v1 = Vector(10,20)
v2 = Vector(50,60)
v3 = v1 + v2

# print(v3) -This will show the string if you have __repr__ function other wise it will show the
# location of the object in memory

# print(v3.x)
# print(v3.y)

# print(len(v3))

v3()