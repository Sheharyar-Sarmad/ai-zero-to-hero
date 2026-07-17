import time as waqt


class Calculator:

    def __init__(self, choice, number):
        self.choice = choice.lower()
        self.number = number

        print("\n🔄 Processing your request...")
        waqt.sleep(1.5)

    def calculate(self):
        if self.number <= 0:
            print("❌ Negative numbers and 0 are not allowed!")
            return

        if self.choice == "s":
            result = self.number ** 2
            print(f"\n📐 Square of {self.number} is: {result}")

        elif self.choice == "c":
            result = self.number ** 3
            print(f"\n📦 Cube of {self.number} is: {result}")

        else:
            print("❌ Invalid choice! Please enter 's' for square or 'c' for cube.")

    def showInfo(self):
        print("\n✨ Calculation Complete!")
        print("══════════════════════════")
        waqt.sleep(1)


# 🔹 User Input
print("🔢 Welcome to Smart Calculator 🔢")
choice = input("👉 Enter 's' for Square or 'c' for Cube: ")
number = int(input("👉 Enter a positive number: "))

# 🔹 Object Creation
calc = Calculator(choice, number)

# 🔹 Perform Calculation
calc.calculate()
calc.showInfo()