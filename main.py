class BankAccount:
    def __init__(self):
        self.name = ""
        self.account_number = "4355400938"
        self.balance = 0
<<<<<<< HEAD
=======
        self.__interest_rate = 0.005
>>>>>>> 905202859c66da4b3d85303e62ec5e051f05d410
        print("Hello!! Welcome to the Deposit and Withdrawal Machine")

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, Deposited {amount} $. Current balance is: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name}, Withdraw {amount} $. Current balance is: {self.balance}")

        else:
            print("You don't have enough funds to withdraw")
<<<<<<< HEAD
=======

    def get_interest_rate(self):
        return self.__interest_rate


>>>>>>> 905202859c66da4b3d85303e62ec5e051f05d410
