# 12. Demonstrate inheritance by creating a class SavingsAccount that adds interest calculation to BankAccount.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    def check_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

acc = SavingsAccount(1000, 0.05)
acc.add_interest()
print(acc.check_balance())  # Output: 1050