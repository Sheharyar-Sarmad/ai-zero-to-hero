


import json
marksDictionary = {}  # empty dictionary

name = input("Enter your name: ")
marks1 = int(input("Enter number 1: "))
marks2 = int(input("Enter number 2: "))
marks3 = int(input("Enter number 3: "))

# Check for total percentage
total_percentage = (marks1 + marks2 + marks3) / 3 
# or else (100*(marks1+marks2+marks3))/300

total_percentage = round(total_percentage , 2)

if total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("You are pass", total_percentage)

else:
    print("You are failed", total_percentage)

marksDictionary.update(
    {
        "Name": name,
        "Marks1": marks1,
        "Marks2": marks2,
        "Marks3": marks3,
        "TotalPercentage": total_percentage,
    }
)

print(json.dumps(marksDictionary, indent=4, ))