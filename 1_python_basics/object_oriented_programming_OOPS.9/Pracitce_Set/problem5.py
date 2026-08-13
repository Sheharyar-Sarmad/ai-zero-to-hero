class Train:

    def __init__(self, train_name, total_seats):
        self.train_name = train_name
        self.total_seats = total_seats
        self.booked_seats = 0

    def book(self, name, time):
        if name == "" or time == "":
            print("\nPlease enter full credentials!\n")
            return

        if self.booked_seats >= self.total_seats:
            print("\nAll tickets are reserved!\n")
        else:
            self.booked_seats += 1
            print(f"\nCongratulations {name}!")
            print(f"Your booking is confirmed at {time}")
            print(f"Remaining seats: {self.total_seats - self.booked_seats}\n")

    def getStatus(self):
        print("\nTrain Name:", self.train_name)
        print("Total Seats:", self.total_seats)
        print("Booked Seats:", self.booked_seats)
        print("Available Seats:", self.total_seats - self.booked_seats)

    def getFare(self, where, to):
        fare = 500  # fixed for now
        print(f"\nFrom {where} to {to}")
        print(f"Fare is: Rs {fare}\n")


# ----------- USER OUTPUT ------------

train1 = Train("Green Express", 3)

train1.book("Ali", "10:00 AM")
train1.book("Ahmed", "12:00 PM")
train1.getStatus()
train1.getFare("Lahore", "Karachi")