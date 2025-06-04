# 11. Create a class BankAccount with methods to deposit, withdraw, and check balance, raising an exception for insufficient funds.
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    def check_balance(self):
        return self.balance

acc = BankAccount()
acc.deposit(100)
print(acc.check_balance())  # Output: 100
acc.withdraw(50)
print(acc.check_balance())  # Output: 50
try:
    acc.withdraw(100)
except ValueError as e:
    print(e)  # Output: Raises Exception