class BankAccount:
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount. Deposit amount must be greater than zero."
        self.balance += amount
        return f"Successfully deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount. Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Successfully withdrawn ${amount}. New balance: ${self.balance}"

    def modify_account(self, new_name=None, new_pin=None):
        if new_name:
            self.name = new_name
        if new_pin:
            self.pin = new_pin
        return "Account details updated successfully."

    def close_account(self):
        self.name = None
        self.pin = None
        self.balance = None
        return "Account closed successfully."


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, pin, initial_deposit=0.0):
        if name in self.accounts:
            return "Account with the same name already exists. Please choose a different name."
        account = BankAccount(name, pin, initial_deposit)
        self.accounts[name] = account
        return f"Account created successfully. Account Name: {name}, Account PIN: {pin}"

    def get_account(self, name):
        if name not in self.accounts:
            return "Account not found. Please check the account name and try again."
        return self.accounts[name]

    def close_account(self, name):
        if name not in self.accounts:
            return "Account not found. Please check the account name and try again."
        account = self.accounts.pop(name)
        return account.close_account()


def main():
    bank = Bank()
    while True:
        print("Welcome to Online Banking!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            pin = input("Enter your PIN: ")
            initial_deposit = float(input("Enter initial deposit amount (optional): ")) or 0.0
            print(bank.create_account(name, pin, initial_deposit))
        elif choice == "2":
            name = input("Enter your name: ")
            pin = input("Enter your PIN: ")
            account = bank.get_account(name)
            if not account or account.pin != pin:
                print("Invalid name or PIN. Please try again.")
                continue
            while True:
                print("Welcome, {}!".format(account.name))
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Modify Account")
                print("5. Close Account")
                print("6. Logout")
                inner_choice = input("Enter your choice: ")
                if inner_choice == "1":
                    print("Current Balance: ${}".format(account.check_balance()))
                elif inner_choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    print(account.deposit(amount))
                elif inner_choice == "3":
                    amount = float(input("Enter withdrawal amount:"))
                    withdraw(self, amount)
                elif inner_choice == "4":
                    modify_account()
                elif inner_choice == "5":
                  close_pin = input(print('Enter PIN to securely close account:'))
                  if close_pin == self.pin:
                    close_account()
                  else:
                    print('Account closed unsuccessfully.')
                    main()

main()
                    
              
            

