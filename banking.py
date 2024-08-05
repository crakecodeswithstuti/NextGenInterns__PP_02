class BankAccount: 
    def __init__(self, account_number, balance=0): 
        self.account_number = account_number 
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} successful. New balance: {self.balance}"
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. New balance: {self.balance}"
        else:
            return "Insufficient funds"
    def check_balance(self):
        return f"Account Balance: {self.balance}"
account1 = BankAccount("12345")
print(account1.deposit(1000)) 
print(account1.check_balance()) 
print(account1.withdraw(500)) 
print(account1.check_balance())