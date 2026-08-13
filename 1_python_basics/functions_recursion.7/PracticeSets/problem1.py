
# MY LOGIC LONG ONE BUT MORE GOOD FOR LOGIC BUILDING :


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 1st number: "))
# c = int(input("Enter 1st number: "))

# def greatestNum() :
#     if(a == b or b == c or a == c ) : 
#         print("Same values are not allowed")

#     elif(a<0 or b<0 or c<0) :
#         print("Negative values are not allowed")

#     elif((a==b or b==c or a==c) and (a<0 or b<0 or c<0)) :
#         print("Negative and same values are not allowed")

#     elif(a>b and a>c) :
#         print(f"a variable is the greatest number: {a} its the number")

#     elif(b>a and b>c) :
#         print(f"b is the greatest number: {b} its the number")

#     elif(c>b and c>a) :
#         print(f"c is the greatest number: {c} its the number")

#     else : 
#         print("Write some number to done some tasks")

# greatestNum()

# print("Thanks for using your program")
# print('Programm created by Sheharyar Sarmad Python dev')


# Small piece of code and also good :

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))

# def GreatestNumber() :
#     if a<0 or b<0 or c<0 :
#         print("Negative values are allowed")
#     elif a==b or b==c or a==c :
#         print("Some values provided by you are same")
#     else :
#         print(f"Greatest number is {max(a , b , c)}")

# GreatestNumber()
# print("Thanks this programm is created by Sheharyar")


# Again my logic more convinient way and reusable code which is used in industry:


# def GreatestNum(a , b , c) :
#     if(a<0 or b<0 or c<0) :
#         return "Negative values are not allowed" 

#     elif(a == 0 or b == 0 or c == 0) :
#         return "Zero(0) number is not allowed"
    
#     elif(a == b or b == c or a == c) :
#         return "Values(integers) provided by you are same.\n its not allowed"

#     else :
#         return f"Greatest number is {max(a , b , c)}"

# a = int(input('Enter 1st number </>: '))
# b = int(input('Enter 2st number </>: '))
# c = int(input('Enter 3st number </>: '))

# print(GreatestNum(a , b , c))