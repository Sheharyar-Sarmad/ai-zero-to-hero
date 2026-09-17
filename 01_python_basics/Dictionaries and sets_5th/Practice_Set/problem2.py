# using add method
s = set()

n = int(input("Enter number 1: "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number 3: "))
s.add(n)
n = int(input("Enter number 4: "))
s.add(n)
n = int(input("Enter number 5: "))
s.add(n)
n = int(input("Enter number 6: "))
s.add(n)
n = int(input("Enter number 7: "))
s.add(n)
n = int(input("Enter number 8: "))
s.add(n)

print(s)

# Using update method:

s = set()
numbers = []

numbers.append(int(input("Enter number 1: ")))
numbers.append(int(input("Enter number 2: ")))
numbers.append(int(input("Enter number 3: ")))
numbers.append(int(input("Enter number 4: ")))
numbers.append(int(input("Enter number 5: ")))
numbers.append(int(input("Enter number 6: ")))
numbers.append(int(input("Enter number 7: ")))
numbers.append(int(input("Enter number 8: ")))

s.update(numbers)

print(s)