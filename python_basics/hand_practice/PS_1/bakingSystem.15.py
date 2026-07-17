# Mini Banking System

accounts = {}  # Store all accounts

def create_account():
    username = input("Enter a new username: ")
    if username in accounts:
        print("Username already exists!\n")
        return
    pin = input("Set a 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be 4 digits!\n")
        return
    balance = float(input("Enter initial deposit amount: "))
    accounts[username] = {
        "pin": pin,
        "balance": balance,
        "transactions": [f"Account created with balance {balance:.2f}"]
    }
    print(f"Account for {username} created successfully!\n")

def login(username):
    if username not in accounts:
        print("Username not found!\n")
        return False
    pin = input("Enter PIN: ")
    if pin != accounts[username]["pin"]:
        print("Incorrect PIN!\n")
        return False
    return True

def deposit():
    username = input("Enter username: ")
    if not login(username):
        return
    amount = float(input("Enter deposit amount: "))
    accounts[username]["balance"] += amount
    accounts[username]["transactions"].append(f"Deposited {amount:.2f}, new balance {accounts[username]['balance']:.2f}")
    print(f"{amount:.2f} deposited successfully!\n")

def withdraw():
    username = input("Enter username: ")
    if not login(username):
        return
    amount = float(input("Enter withdrawal amount: "))
    if amount > accounts[username]["balance"]:
        print("Insufficient balance!\n")
        return
    accounts[username]["balance"] -= amount
    accounts[username]["transactions"].append(f"Withdrew {amount:.2f}, new balance {accounts[username]['balance']:.2f}")
    print(f"{amount:.2f} withdrawn successfully!\n")

def transfer():
    sender = input("Enter your username: ")
    if not login(sender):
        return
    receiver = input("Enter receiver's username: ")
    if receiver not in accounts:
        print("Receiver username not found!\n")
        return
    amount = float(input("Enter amount to transfer: "))
    if amount > accounts[sender]["balance"]:
        print("Insufficient balance!\n")
        return
    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount
    accounts[sender]["transactions"].append(f"Transferred {amount:.2f} to {receiver}, new balance {accounts[sender]['balance']:.2f}")
    accounts[receiver]["transactions"].append(f"Received {amount:.2f} from {sender}, new balance {accounts[receiver]['balance']:.2f}")
    print(f"{amount:.2f} transferred to {receiver} successfully!\n")

def transaction_history():
    username = input("Enter username: ")
    if not login(username):
        return
    print(f"\n--- Transaction History for {username} ---")
    for txn in accounts[username]["transactions"]:
        print(txn)
    print("--------------------------------------\n")

def main():
    while True:
        print("=== Mini Banking System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()