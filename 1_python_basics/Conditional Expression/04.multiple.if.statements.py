a = int(input("Enter your age: "))

# if elif else ladder:  

# important note: if didnt need else statement to work but else do need if statement to run. conclusion says: if is independent but else and elif are not independent they if to run the proggramm 

# if statement one:
if(a%2 == 0) :
    print("a is even")
else :
    print("a is odd")
# End of if statement no 1

# if statement two:
if (a>=18) :
    print("You are above the age of consent")
    print("Good for you")

elif(a == 0) :
    print("You entered zero(0) as age")

elif(a<0) :
    print("You are entering the invalid negative age")

else:
    print("You are below the age of consent")
# End of if statement no 2

print("End of programm")