

# Dunder Methods:

# Dunder methods are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__, __len__).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __len__(self):
        return self.age

# Usage
p1 = Person("Ali", 25)
print(p1)        # Calls __str__ -> "Ali is 25 years old."
print(len(p1))   # Calls __len__ -> 25