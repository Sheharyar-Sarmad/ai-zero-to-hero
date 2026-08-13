"""
1 for Snake
-1 for Water
0 for Gun
"""

import time
import random

print("")
print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
print("")
print("Please enter: ")
print("")
print("s for Snake 🐍")
print("w for Water 💧")
print("g for Gun 🔫")
print("")

computer = random.choice([1, 0, -1])

yourstr = input("👉 Enter your choice (s/w/g): ").lower().strip()

yourDic = {"s": 1, "w": -1, "g": 0}
# By now we have 2 numbers(variables) you and computer

reverseDict = {
    1: "Snake 🐍",
    -1: "Water 💧",
    0: "Gun 🔫"
}

# 🔒 Input Validation (Prevents KeyError)
if yourstr not in yourDic:
    print("❌ Invalid input! Please enter only s, w, or g.")
else:
    you = yourDic[yourstr]

    print(f"\n🧍 You chose: {reverseDict[you]}")
    print(f"💻 Computer chose: {reverseDict[computer]}")
    print("")
    
    time.sleep(1)

    if computer == you:
        print("🤝 It's a Draw!")
        print("")
        
    else:
        if computer == -1 and you == 1:
            print("🎉 You Win!")
            print("")

        elif computer == -1 and you == 0:
            print("😢 You Lose!")
            print("")

        elif computer == 1 and you == -1:
            print("😢 You Lose!")
            print("")

        elif computer == 1 and you == 0:
            print("🎉 You Win!")
            print("")

        elif computer == 0 and you == 1:
            print("😢 You Lose!")
            print("")

        elif computer == 0 and you == -1:
            print("🎉 You Win!")
            print("")

        else:
            print("⚠ Something went wrong!")
            print("")

print("Thanks 🐍 for playing this game")
print("Developed </> by Sheharyar Sarmad")
print("")