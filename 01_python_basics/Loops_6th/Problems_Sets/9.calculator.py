


print("For addition(+) enter 1")
print("For subtraction(-) enter 2")
print("For multiplication(*) enter 3")
print("For division(/) enter 4")

choice = int(input("Enter your choice in (0-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = float(num1 + num2)
    print(f"{num1} + {num2} = {result}")

elif choice == 2:
    result = float(num1 - num2)
    print(f"{num1} - {num2} = {result}")

elif choice == 3:
    result = float(num1 * num2)
    print(f"{num1} * {num2} = {result}")

elif choice == 4:
    if num2 != 0:
        result = float(num1 / num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero!")

else:
    print(f"Invalid choice: ", choice)
    print("Select these:")
    print("For addition(+) enter 1")
    print("For subtraction(-) enter 2")
    print("For multiplication(*) enter 3")
    print("For division(/) enter 4")
