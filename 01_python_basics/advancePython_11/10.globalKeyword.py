# This variable is a global variable and we can use it in any function class or anywhere

a = 89
# But local variables are those which we cant use outside of their range.

# For example: the variables we create in functions and classes or in if_elif_else are called local variable and their score is just inside their range.

def fun() :
    # When we say global then we are saying that i am changing the global variable named as (a)
    global a 
    a = 3
    # It will print 3 because a is inside the function is the local variable
    print(a)

fun()
print(a)