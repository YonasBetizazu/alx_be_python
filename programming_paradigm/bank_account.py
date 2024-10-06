class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance  # Private attribute for account balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount  # Update the balance
            print(f"Deposited: ${amount:.1f}. New balance: ${self.__account_balance:.1f}")  
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:  
            self.__account_balance -= amount  # Update the balance
            return True  # Withdrawal successful
        elif amount > self.__account_balance:
            print("Insufficient funds.")
            return False  # Withdrawal failed
        else:
            print("Something went wrong!")  
            return False  # Withdrawal failed

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")  
