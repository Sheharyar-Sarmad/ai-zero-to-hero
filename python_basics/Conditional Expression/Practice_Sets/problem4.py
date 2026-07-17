# my logic and code

a = input("Enter your name: ")

lengthOfA = len(a)

if(lengthOfA >= 10) :
    print('The username contains 10 or more than ten characters' , a)
elif(lengthOfA > 0 ) :
    print('The length of the username is less than than' , a) 
else :
    print("Username cannot be empty")

# Ai code and logic
a = input("Enter your name: ")

lengthOfA = len(a)

if lengthOfA >= 10:
    print("The username contains 10 or more characters:", a)

elif lengthOfA > 0:
    print("The username contains less than 10 characters:", a)

else:
    print("Username cannot be empty")


# Harry bhai code

usename = input("Enter your username: ")

if(len(usename) < 10) :
    print("Your username contains less than 10 characters")
else :
    print("All is well")
