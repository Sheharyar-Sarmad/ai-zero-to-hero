def startUp():
    print("\nWelcome to our app!\n")
    print("You can find the even and the odd number in this program\n")


def findEorO(n: int) -> str:
    try:
        if n <= 0:
            return "Error: Zero or negative values are not allowed"

        elif n % 2 == 0:
            return f"\nYes the number is even!\n{n} is an even number\n"

        else:
            return f"\nThe number is odd!\n{n} is an odd number\n"

    except Exception as e:
        return f"Error coming and saying: {e}"


def endUp():
    print("\nThis program is created by Sheharyar Sarmad\nCEO of Webora Labs born in 10/Aug/2010\n")


if __name__ == "__main__":
    startUp()

    n = int(input("Enter your number: "))
    print(findEorO(n))

    endUp()