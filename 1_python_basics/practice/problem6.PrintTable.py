def printTable(n: int):
    if not isinstance(n, int):
        return f"Type error! Only integers are allowed. You entered: {n}"
    if n <= 0:
        return "0 or negative values are not allowed!"
    
    print(f"\nMultiplication Table of {n}:\n")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


def greet():
    print("\nThis program prints the multiplication table you want.")
    print("Program created by Sheharyar Sarmad\n")


# Input
try:
    n = int(input("Enter your number: "))
    result = printTable(n)
    if result:  # If there is an error message returned
        print(result)
except ValueError:
    print("Invalid input! Please enter an integer.")

greet()