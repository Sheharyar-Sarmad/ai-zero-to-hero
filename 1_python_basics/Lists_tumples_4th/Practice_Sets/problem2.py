# Ai logic
marks = []

m1 = int(input("Enter first marks: "))
m2 = int(input("Enter second marks: "))
m3 = int(input("Enter third marks: "))
m4 = int(input("Enter fourth marks: "))
m5 = int(input("Enter fifth marks: "))
m6 = int(input("Enter sixth marks: "))

marks.extend([m1, m2, m3, m4, m5, m6])

# Sort in descending order (big → small)
marks.sort( reverse=True )

print("Sorted marks (Highest to Lowest):", *marks)

# Harry bhai logic
marks = []

m1 = int(input("Enter your number here: "))
marks.append(m1)
m2 = int(input("Enter your number here: "))
marks.append(m2)
m3 = int(input("Enter your number here: "))
marks.append(m3)
m4 = int(input("Enter your number here: "))
marks.append(m4)
m5 = int(input("Enter your number here: "))
marks.append(m5)
m6 = int(input("Enter your number here: "))
marks.append(m6)

marks.sort()

print(marks)

# my logic
marks = []

m1 = int(input('Enter your marks here: '))
m2 = int(input('Enter your marks here: '))
m3 = int(input('Enter your marks here: '))
m4 = int(input('Enter your marks here: '))
m5 = int(input('Enter your marks here: '))
m6 = int(input('Enter your marks here: '))

marks.extend([m1 , m2 , m3 , m4 , m5 , m6])
marks.sort()

print(*marks)
