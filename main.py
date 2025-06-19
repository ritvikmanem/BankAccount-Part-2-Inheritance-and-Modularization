class BankAccount():
    bank_name = "BOFA"
    def __init__(self, customer_name, account_balance, minimum_balance):
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.minimum_balance = minimum_balance

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


# Justin will do the checking account, account number and routing.
class Checking:

    balance = 0

    def __init__(self, transfer_limit):
        self.__account_number = 10377465547755665
        self.transfer_limit = transfer_limit
        self.balance = 0

    def transfer_in(self, amount):
        if amount > self.transfer_limit:
            print(f"Error cannot transfer that amount must be lower than {self.transfer_limit}")
        else:
            self.balance += amount

    def transfer_out(self, amount):
        if amount > self.transfer_limit:
            print(f"Error cannot transfer that amount must be lower than {self.transfer_limit}")
        else:
            self.balance -= amount
            return amount



    

bill = BankAccount("Bill", 1000, 100)
bill.print_customer_information()
bill.deposit(500)
bill.withdraw(200)
bill.print_customer_information()

bob = BankAccount("Bob", 2000, 200)
bob.print_customer_information()
bob.withdraw(500)
bob.deposit(300)
bob.print_customer_information()