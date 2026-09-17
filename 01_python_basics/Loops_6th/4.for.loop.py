
# A for loop is used to iterate trough a sequence like lists, tuples , or strings[iterables]

for i in range(1000) :
    print("I love you ❤️ 🎀")

l = [9 , 0 ,8]

for item in l :
    print(item)


# 🔹 What is step size in Python?
# Step size means:
# How much to jump forward each time in a loop or slice
# It is mostly used in:
# range()
# String slicing
# List slicing

for me in range(0 , 10 , 1) : 
# What happens here?
# Start = 0
# Stop = 10
# Step = 1 # means jump 2 digits for each time whenever the loop runs or execute
    print(me)