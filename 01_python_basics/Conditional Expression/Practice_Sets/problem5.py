#MY LOGIC:
l = ["Harry" , "Subham" , "Chatgpt" , "Sheharyar" , "Diwya"]

name = input("Enter your username: ")

if(name in l) :
    print("Your username is already in the list" , name )
elif(name not in l) :
    print("Your name is not in the list",name)
else :
    print("You didnt enter any username")

# AI LOGIC
if name in l:
    print("Already in list")
else:
    print("Not in list")