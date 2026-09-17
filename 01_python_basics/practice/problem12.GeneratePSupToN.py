from json import dumps

def generatePSupToN(n):
    try:
        if not isinstance(n, int):
            return "Only integers are allowed!"
        if n <= 0:
            return "0 or Negative values are not allowed!"

        squares = []
        for i in range(1, n+1):
            square = i * i
            print(f"The perfect square of {i} is {square}")
            squares.append(square)
        return dumps(squares , indent=2)

    except Exception as e:
        return f"An error occurred: {e}"


n = int(input("Enter a number to generate perfect squares up to: "))
result = generatePSupToN(n)
print("All perfect squares:", result)