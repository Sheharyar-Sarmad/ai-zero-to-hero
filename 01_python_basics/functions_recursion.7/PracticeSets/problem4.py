



'''
sum(1) = 1
sum(2) = 2 + 1 
sum(3) = 3 + 2 + 1
sum(4) = 4 + 3 + 2 + 1
sum(5) = 5 + 4 + 3 + 2 + 1

sum(n) = 1 + 2 + 3 + 4 + 5.....n
'''
import sys
sys.setrecursionlimit(2000)

def sum_n(n) :
    if (n == 1) :
        return 1
    elif(n<0) :
        return "Negative integers are not allowed"
    else : 
        return sum_n(n - 1) + n

num = int(input("Enter your number: "))
print(sum_n(num))
