

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a == 0 or b == 0 :
    raise ZeroDivisionError("Hey our program is not meant to divide the values by zero(0)")

else :
    print(f"The division of a/b is {float(a/b)}")