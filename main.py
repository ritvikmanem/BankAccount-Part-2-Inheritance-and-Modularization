from BankAccount import BankAccount
from Checking import Checking
from Savings import Savings

# Justin will do the checking account, account number and routing.
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

#test

# Marquis will do savings account with interest
