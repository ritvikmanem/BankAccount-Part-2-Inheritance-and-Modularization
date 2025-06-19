class BankAccount():
    bank_name = "BOFA"
    def __init__(self, customer_name, account_balance, minimum_balance):
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.minimum_balance = minimum_balance
        self._routing_number = 123456789

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance: {self.account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and (self.account_balance - amount) >= self.minimum_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self.account_balance}")
        else:
            print("Withdrawal amount exceeds the minimum balance requirement or is not positive.")

    def print_customer_information(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Balance: {self.account_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Bank Name: {self.bank_name}")