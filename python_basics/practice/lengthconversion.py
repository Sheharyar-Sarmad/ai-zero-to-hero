def starter():
    print("\nConvert the values into km, m, cm, mm")
    print("It will convert a given value into remaining 3 values")
    print("Select:")
    print("1 for km")
    print("2 for m")
    print("3 for cm")
    print("4 for mm")


def convertVal(choice, amount):
    try:
        if choice == 1:  # KM
            print(f"\n{amount} km =")
            print(f"{amount * 1000} m")
            print(f"{amount * 100000} cm")
            print(f"{amount * 1000000} mm")

        elif choice == 2:  # Meter
            print(f"\n{amount} m =")
            print(f"{amount / 1000} km")
            print(f"{amount * 100} cm")
            print(f"{amount * 1000} mm")

        elif choice == 3:  # Centimeter
            print(f"\n{amount} cm =")
            print(f"{amount / 100000} km")
            print(f"{amount / 100} m")
            print(f"{amount * 10} mm")

        elif choice == 4:  # Millimeter
            print(f"\n{amount} mm =")
            print(f"{amount / 1000000} km")
            print(f"{amount / 1000} m")
            print(f"{amount / 10} cm")

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)


def main():
    while True:
        starter()

        try:
            choice = int(input("Enter your choice (1-4): "))
            amount = float(input("Enter value: "))

            convertVal(choice, amount)

            again = input("\nDo another conversion? (y/n): ").lower()
            if again != "y":
                print("Exiting program...")
                break

        except ValueError:
            print("Please enter valid numbers!")


if __name__ == "__main__":
    main()