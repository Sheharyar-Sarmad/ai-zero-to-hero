number = int(input("Enter the number for reverse printing: "))

for i in range(number , 0 , -1) :
    print(f"{i} ⏩ {type(i).__name__}") 