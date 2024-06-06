class ChildrensAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.interest_rate = 0.007  # 0.7% interest rate

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        else:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest} applied. New balance: ${self.balance}"

    def check_balance(self):
        return f"Current balance: ${self.balance}"


if __name__ == "__main__":
    child_account = ChildrensAccount()
    print(child_account.check_balance())

    print(child_account.deposit(10000))
    print(child_account.check_balance())

    print(child_account.apply_interest())
    print(child_account.check_balance())
