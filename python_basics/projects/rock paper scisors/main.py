import random

def start_up():
    print("\nWelcome to Rock Paper Scissors!\n")
    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissors")
    print("Type 'exit' to quit the game.\n")

def end_up():
    print("\nThanks for playing our game!\n")
    print("Developed by Sheharyar Sarmad ❤️")
    print("Bye Bye!")

def game(userChoice: int, compChoice: int):
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }

    userChoiceText = choices[userChoice]
    compChoiceText = choices[compChoice]

    if userChoice == compChoice:
        return f"🤝 Match Drawn! You chose {userChoiceText} and computer chose {compChoiceText}"

    elif (
        (userChoice == 1 and compChoice == 3) or
        (userChoice == 2 and compChoice == 1) or
        (userChoice == 3 and compChoice == 2)
    ):
        return f"🎉 You Win! You chose {userChoiceText} and computer chose {compChoiceText}"

    else:
        return f"💻 Computer Wins! You chose {userChoiceText} and computer chose {compChoiceText}"


start_up()

while True:
    userInput = input("\nEnter your choice (1-3) or 'exit': ").lower()

    if userInput == "exit":
        end_up()
        break

    try:
        userChoice = int(userInput)

        if userChoice not in [1, 2, 3]:
            print("Please enter 1, 2, or 3.")
            continue

        compChoice = random.randint(1, 3)

        print(game(userChoice, compChoice))

    except ValueError:
        print("Invalid input. Enter 1, 2, 3, or exit.")