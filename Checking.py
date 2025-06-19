from BankAccount import BankAccount
# Justin will do the checking account, account number and routing.
class Checking(BankAccount):

    balance = 0

    def __init__(self, customer_name, account_balance, minimum_balance):
        super(Checking, self).__init__(customer_name, account_balance, minimum_balance)
        self.__account_number = 644879392 # place holder
        self.transfer_limit = minimum_balance
        self.balance = account_balance

    def transfer_in(self, amount):
        if amount > self.transfer_limit:
            print(f"Error cannot transfer that amount must be lower than {self.transfer_limit}")
        else:
            self.balance += amount # adding the amount that was transferred to the checking accounts internal balance

    def transfer_out(self, amount):
        if amount > self.transfer_limit:
            print(f"Error cannot transfer that amount must be lower than {self.transfer_limit}")
        else:
            self.balance -= amount
            return amount # amount returned to be transferred into another account