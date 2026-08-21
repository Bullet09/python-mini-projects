balance = 10000


def check_balance():
    print("\n===== BALANCE =====")
    return


def deposit(amount_deposit, balance):
    amount_deposit = int(input("\nEnter amount to deposit: "))
    new_balance = amount_deposit + balance
    return new_balance


def withdraw():
    amount_withdraw = int(input("Enter amount to withdraw: "))

    if amount_withdraw > balance:
        print("\nInsufficient balance!")
    elif amount_withdraw < balance:
        print("\nWithdrawal successful!")
        total = amount_withdraw - balance
        print("Remaining balance: ", total)

    else:
        print("invalid")


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
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid option")
