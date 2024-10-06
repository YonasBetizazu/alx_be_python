class BankAccount:
    def __init__(self,account_balance=0):
        self.__account_baclance=account_balance
    def deposit(self,amount):
        if amount>0:
            self.__account_baclance+=amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.__account_baclanc:.2f}")
        else:
            print("please enter Valid amount")
    def withdraw(self,amount):
        if 0<amount<self.__account_baclanc:
            self.__account_baclanc-=amount
        elif amount>self.__account_baclanc:
            print("You don't have sufficient amount of money in your balance")
        else:
            print("someting went worong!")
    def display_balance(self):
         print(f"Your Balance is {self.__account_baclanc:.2f}")
