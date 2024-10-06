class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance  

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount  
            print(f"Deposited: ${amount:.2f}. New balance: ${self.__account_balance:.2f}")  
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:  
            self.__account_balance -= amount  #
            return True  # Withdrawal successful
        elif amount > self.__account_balance:
            print("You don't have sufficient funds.")
            return False  # Withdrawal failed
        else:
            print("Something went wrong!")  
            return False  # Withdrawal failed

    def display_balance(self):
        """Print the current account balance."""
        print(f"Your balance is ${self.__account_balance:.2f}")  
