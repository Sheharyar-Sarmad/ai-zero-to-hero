# # Ai logic
# import random
# import time as waqt


# def gameInfo():
#     print("\n Welcome to THE PERFECT GUESS!")
#     print(" Guess the number between 1 and 100")
#     print(" You have 10 chances\n")


# def perfectGuess():
#     comNum = random.randint(1, 100)
#     # print(comNum)
#     chances = 10

#     while chances > 0:
#         try:
#             userNum = int(input("Enter your guess: "))

#             if userNum < 1 or userNum > 100:
#                 print("⚠ Please enter number between 1 and 100!")
#                 continue

#         except ValueError:
#             print(" Only integer numbers are allowed!")
#             continue

#         if userNum == comNum:
#             print("\n Congratulations! You guessed correctly!")
#             print("Computer number was:", comNum)
#             return

#         elif userNum > comNum:
#             print(" Too high!")

#         else:
#             print(" Too low!")

#         chances -= 1
#         print("Remaining chances:", chances)
#         print("-" * 30)

#     print("\n You lost the game!")
#     print("Correct number was:", comNum)


# # Run Game
# gameInfo()
# perfectGuess()




# My logic (Fixed but same structure)

# import time
# from random import randint

# def aboutGame():
#     print("\n Welcome to THE PERFECT GUESS!")
#     print(" Guess the number between 1 and 100")
#     print(" You have 10 chances\n")


# def gameLogic(num, comNum):

#     try:
#         time.sleep(1)

#         if comNum == "":
#             print("Game error! Computer didn't generate any number!")
#             return

#         userLifeCount = 10

#         while userLifeCount > 0:

#             try:
#                 time.sleep(1)

#                 # 🔥 Take input inside loop (important fix)
#                 num = int(input("Enter your number: "))

#                 # 🔥 Correct range condition
#                 if num < 1 or num > 100:
#                     print("Please enter values between 1 to 100!")
#                     continue

#                 elif num == comNum:
#                     print("Congratulations you won!")
#                     print(f"You guessed the right number.")
#                     print(f"Your number was {num} and computer number was also {comNum}")
#                     return  # stop game

#                 elif num > comNum:
#                     print("Your number is too high!")

#                 else:
#                     print("Your number is too low!")

#                 userLifeCount -= 1
#                 print(f"{userLifeCount} chances are left for you now!")
#                 print("-" * 30)

#             except ValueError:
#                 print("Only integers are allowed!")

#         print("You lose!")
#         print(f"Computer number was {comNum}")

#     except Exception as e:
#         print(f"Error says {e}")


# computerNumber = randint(1, 100)

# aboutGame()
# gameLogic("", computerNumber)