from main import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.balance = self.balance
        self.interest_rate = 0.005

    def deposit(self, amount):
        interest_amount = amount * self.interest_rate
        self.balance += interest_amount
        self.balance += amount
        print(f"{self.name},Deposited $ {amount} . current balance is: {self.balance}(including interest)")

    def withdraw(self, amount):
        if amount <= 700000:
            if amount >= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds. Account balance is ", self.balance)
        else:
            print("withdrawal amount exceeds the limit of $700000")


savings_account = SavingsAccount("student")
savings_account.deposit(1000)
