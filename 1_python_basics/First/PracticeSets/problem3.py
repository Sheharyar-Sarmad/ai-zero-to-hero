import pyttsx3

engine = pyttsx3.init()
engine.say('''


You said:
Enter 1st number: 12
Enter 2nd number: 12
Enter 3rd number: 3
9.0
Thanks you
Enter 1st number: 21
Enter 2nd number: 2
Enter 3rd number: 1
8.0
Thanks you
Enter 1st number: 2
Enter 2nd number: 1
Enter 3rd number: 2
1.667
Thanks you
Enter 1st number: 1
Enter 2nd number: 2
Enter 3rd number: 12
5.0
Enter 1st number: 2
Enter 2nd number: 1
Enter 3rd number: 21
8.0
Thanks you thats the output and thats the code 

def avg():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))

    return round(((a + b + c) / 3), 3)


for i in range(5):
    result = avg()
    print(result)
    if (i == 3) :
        pass
    else :
        print("Thanks you")

ChatGPT said:
Your code is working correctly 👍 — let’s understand why the output looks like that.

✅ What Your Code Does
1️⃣ Function avg()
Takes 3 numbers from the user

Calculates their average:

(a + b + c) / 3
Rounds it to 3 decimal places

Returns the result

2️⃣ This Loop:
for i in range(5):
This means:

The program will run 5 times

Each time it will ask for 3 numbers again

So that's why you see the input prompts repeating.

3️⃣ About This Part:
if (i == 3) :
    pass
else :
    print("Thanks you")
🔹 What pass means:
It does nothing.

So when i == 3 (4th loop run):

It prints the average

But it does NOT print "Thanks you"

🟢 Why "Thanks you" Is Missing Once?
Because of this condition:

if (i == 3)
In range(5), values of i are:

0, 1, 2, 3, 4
So when i = 3, it skips printing "Thanks you".

🔥 Small Improvement
If you want "Thanks you" to print every time, just remove the if-else:

for i in range(5):
    result = avg()
    print(result)
    print("Thank you")
⚠️ One More Thing
You wrote:

Thanks you
Correct spelling is:

Thank you
🎯 Your Code Level
For a beginner, this is very good practice:

Functions ✅

Loops ✅

Type conversion (float) ✅

round() function ✅

Conditional statements ✅

You're learning properly 👏

If you want, I can also:

Improve this code

Or explain how to make it more advanced 🚀


You‘re using a less powerful model until your limit resets after 4:51 PM.



''')
engine.runAndWait()