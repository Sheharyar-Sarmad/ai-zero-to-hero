


def pattern(n) :
    if(n == 0) :
        return ""
    else :
        print("*" * n)
        return pattern(n - 1)

num = int(input("Enter your number: "))
pattern(num)


# def reversePattern(n) :
#     if(n == 0) :
#         return ""
#     else :
#         int(n)
#         reversePattern(n - 1) 
#         print("*" * n)

# num = int(input("Enter your number: "))
# reversePattern(num)