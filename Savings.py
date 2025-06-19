from BankAccount import BankAccount

# Marquis will do savings account with interest
class Savings(BankAccount):

    balance = 0

    def __init__(self, customer_name, account_balance, minimum_balance, interest_rate):
        super(Savings, self).__init__(customer_name, account_balance, minimum_balance)
        self.__account_number = 10377465547755665
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.account_balance * (self.interest_rate / 100)
        self.account_balance += interest
        print(f"Interest of {interest} applied. New balance: {self.account_balance}")
