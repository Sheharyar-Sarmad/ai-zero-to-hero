

# A lambda function is a small, anonymous function that can have any number of arguments but can only have one expression.

# Regular function:
def add(x, y):
    return x + y

print(add(5, 3))  # 8

# Lambda function:
add = lambda x, y: x + y
print(add(5, 3))  # 8


# Syntax:
# lambda arguments: expression

# Examples:
lambda x: x * 2           # One argument
lambda x, y: x + y        # Two arguments
lambda x, y, z: x * y * z # Three arguments
lambda: "Hello"           # No arguments
lambda *args: sum(args)   # Variable arguments
lambda **kwargs: kwargs   # Keyword arguments