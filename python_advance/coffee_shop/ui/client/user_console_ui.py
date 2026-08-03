

class ConsoleUIUsers:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def starter():
        print("=" * 60)
        print("☕ Welcome to The Cozy Cup Shop ☕".center(60))
        print("=" * 60)

        print("\nWhere every cup is brewed with care and every visit")
        print("feels like home.\n")

        print("We serve freshly brewed coffee, refreshing beverages,")
        print("and delicious treats made with quality ingredients.\n")

        print("We hope you enjoy your time with us!")
        print("=" * 60)

    def ender(self):
        print("\n" + "=" * 60)
        print("☕ Thank you for visiting The Cozy Cup Shop! ☕".center(60))
        print("=" * 60)
        print("We hope to serve you again soon!\n")
        print(f"🏪 Shop Owner : {self.name}")
        print(f"💻 Software Developed By : {self.name}")
        print("=" * 60)






