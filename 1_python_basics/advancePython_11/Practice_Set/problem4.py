


def divide(n1: int, n2: int) -> float:
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError("Only integers are allowed.")
    
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return n1 / n2


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")

except Exception as e:
    print(f"Error: {e}")