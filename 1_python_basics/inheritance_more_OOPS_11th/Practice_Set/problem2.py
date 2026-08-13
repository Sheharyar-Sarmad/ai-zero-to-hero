class Animals:

    def __init__(self, quantity=0, forSale=0):
        self.quantity = quantity
        self.forSale = forSale

        if self.quantity < 0:
            print("No animals are available right now.")
        else:
            print(f"\nTotal animals available: {self.quantity}")
            print(f"Animals for sale: {self.forSale}")

    def sellAnimals(self, number):
        if number <= self.quantity:
            self.quantity -= number
            print(f"{number} animals sold successfully!")
            print(f"Remaining animals: {self.quantity}")
        else:
            print("Not enough animals available!")


class Pets(Animals):

    def showPets(self, names):
        self.names = names

        if not self.names:
            print("No names available for pets")

        else:
            print("\nThe names of the pets are:")
            for name in self.names:
                print(name, end=" ")
            print()


class Dog(Pets):

    @staticmethod
    def bark():
        print("\nDog says: Woof Woof! 🐶")

    def showBreed(self, breed):
        print(f"Breed of dog: {breed}")


# Creating objects

a = Animals(100, 98)
a.sellAnimals(10)

nameList = [
    "Wolf", "Max", "Bella", "Charlie",
    "Luna", "Rocky", "Daisy",
    "Cooper", "Milo", "Lucy"
]

p = Pets()
p.showPets(nameList)

d = Dog()
d.bark()
d.showBreed("German Shepherd")