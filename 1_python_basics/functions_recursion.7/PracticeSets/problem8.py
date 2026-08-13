

def multiplication(n) :
    for i in range(1 , 11) :
        print(f"{n} X {i} = {n*i} ")
        print("")
    return "Thanks programm is created by Sheharyar"


number = int(input('Enter the number which table you want: '))
print(multiplication(number))