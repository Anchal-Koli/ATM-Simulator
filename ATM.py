import json
import os

# Load Data
if os.path.exists("atm_data.json"):
    with open("atm_data.json", "r") as f:
        data = json.load(f)
else:
    data = {"pin": "1234", "balance": 5000, "transactions": []}

pin = data["pin"]
balance = data["balance"]
transactions = data["transactions"]

print(" Welcome to Python Bank ATM ")

# PIN verification
attempts = 0
while attempts < 3:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin:
        print("\n Login Successful! :) \n")
        break
    else:
        attempts += 1
        print("Wrong PIN! Attempts left:", 3 - attempts)
else:
    print("Too many wrong attempts! Card blocked :(")
    exit()

# ATM Menu
while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")
    print("6. Transaction History")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"💰 Your Balance: ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter deposit amount: ₹"))
        balance += amount
        transactions.append(f"Deposited: ₹{amount}")
        print(f"✅ ₹{amount} deposited successfully! New Balance: ₹{balance}")

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: ₹"))
        if amount <= balance:
            balance -= amount
            transactions.append(f"Withdrawn: ₹{amount}")
            print(f"✅ ₹{amount} withdrawn successfully! Remaining Balance: ₹{balance}")
        else:
            print("❌ Insufficient Balance!")

    elif choice == "4":
        old_pin = input("Enter current PIN: ")
        if old_pin == pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("✅ PIN changed successfully!")
            else:
                print("❌ Invalid PIN format! Must be 4 digits.")
        else:
            print("❌ Incorrect current PIN!")

    elif choice == "5":
        # Save Data before exit
        with open("atm_data.json", "w") as f:
            json.dump({"pin": pin, "balance": balance, "transactions": transactions}, f, indent=4)
        print("👋 Thank you for using Python Bank ATM. Goodbye!")
        break

    elif choice == "6":
        print("\n📜 Transaction History:")
        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions:
                print("-", t)

    else:
        print("⚠️ Invalid choice! Please try again.")
