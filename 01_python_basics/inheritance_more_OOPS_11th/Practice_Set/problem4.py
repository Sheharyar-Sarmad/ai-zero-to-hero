class Number:
    def __init__(self, value):
        self.value = value

    # Addition
    def __add__(self, other):
        return Number(self.value + other.value)

    # Multiplication
    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)


a = Number(5)
b = Number(3)

print("Addition:", a + b)
print("Multiplication:", a * b)