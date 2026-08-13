# My logic
messages = []
malwareComments = []

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if p1 in message:
    print("Malware messages cant add these comments")
    malwareComments.append(p1)
    print(malwareComments)


elif p2 in message:
    print("Malware messages cant add these comments")
    malwareComments.append(p2)
    print(malwareComments)


elif p3 in message:
    print("Malware messages cant add these comments")
    malwareComments.append(p3)
    print(malwareComments)

elif p4 in message:
    print("Malware messages cant add these comments")
    malwareComments.append(p4)
    print(malwareComments)

else:
    print("Comment added")
    messages.append(message)
    print(messages)


print("Programm ended")



# Ai logic:

messages = []
malwareComments = []

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("Malware message cannot be added")

    if p1 in message:
        malwareComments.append(p1)

    if p2 in message:
        malwareComments.append(p2)

    if p3 in message:
        malwareComments.append(p3)

    if p4 in message:
        malwareComments.append(p4)

    print(malwareComments)

else:
    print("Comment added")
    messages.append(message)
    print(messages)

print("Program ended")

# Harry bhaiya logic;

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)) :
    print("This comment is a spam" , message)
else :
    print("This comment is not a spam" , message)

