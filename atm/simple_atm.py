balance = 10000


def check_balance():
    print("\n===== BALANCE =====")
    print("Current balance: ", balance)


def deposit():
    amount_deposit = int(input("\nEnter amount to deposit: "))
    new_balance = amount_deposit + balance
    return new_balance


def withdraw():
    amount_withdraw = int(input("Enter amount to withdraw: "))

    if amount_withdraw == balance:
        exact_withdraw = balance - amount_withdraw
        print("Remaining balance: ", exact_withdraw)
        return exact_withdraw

    elif amount_withdraw < balance:
        amount_deduct = balance - amount_withdraw
        print("\nWithdrawal successful!")
        print("Remaining balance: ", amount_deduct)
        return amount_deduct

    elif amount_withdraw > balance:
        print("\nInsufficient balance!")

    else:
        print("invalid input")


while True:

    print("\n===== SIMPLE ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        new_balance = deposit()
        balance = new_balance
        print("New balance: ", new_balance)

    elif choice == 3:
        new_balance = withdraw()
        balance = new_balance

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option")
