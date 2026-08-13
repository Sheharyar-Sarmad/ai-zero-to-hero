from time import sleep

def startUp():
    print("\nWelcome to the password checker app!")
    print("\nEnter capital letters and special characters(!@#$%^&*) for strong password.")


def logic(password):
    special_char = "!@#$%^&*"

    # Check length
    if len(password) < 8:
        print("Your password is not strong because it must be at least 8 characters!")
        return

    # Check uppercase
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter!")
        return

    # Check special character
    if not any(char in special_char for char in password):
        print("Password must contain at least one special character!")
        return

    print("Your password is STRONG 🔐")


password = input("Enter your password: ")

startUp()
logic(password)