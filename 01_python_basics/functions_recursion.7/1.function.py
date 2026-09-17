# Function is a group of statements performing a specific task:

# When a programm gets bigger and its complexity grows, it gets hard for the programm that what piece of code is doing what

# A function is used by the proggrammer in a programm many certain of times.abs


# for example:


# def avg():
#     a = float(input("Enter 1st number: "))
#     b = float(input("Enter 2nd number: "))
#     c = float(input("Enter 3rd number: "))

#     print(round(((a + b + c) / 3), 3))


# for i in range(5) :
#     i = avg()
#     print(i)


# This avg() is function defination:
# The part containing the exact sets of instructions which are executed during the function call
def avg():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))

    return round(((a + b + c) / 3), 3)


for i in range(5):
    # and this is function call
    result = avg()
    print(result)
    if (i == 3) :
        pass
    else :
        print("Thanks you")