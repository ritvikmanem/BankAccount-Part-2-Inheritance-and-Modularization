from BankAccount import BankAccount
from Checking import Checking
from Savings import Savings

# Part 3. 3 : Senario

print("--> Scenario: Tom creates a checking account with $1200 balance and $100 transfer limit.")
tom_checking = Checking("Tom", 1200, 100)  # $1200 balance with $100 transfer limit
tom_checking.print_customer_information()

print("--> Tom then receives a $150 tranfer.")
tom_checking.transfer_in(150) # then he transfers in $150 but its over the limit

print("--> Tom tries to transfer out $200 (Unsuccessful since its over the limit).")
tom_checking.transfer_out(200)

# Tom successfully transfers out $80
print("--> Then, he tries to transfer out $80 (Successful since its under the limit).")
tom_checking.transfer_out(80)

tom_checking.print_customer_information()
print("\n") 


# Part 4: Two Instances for each class

bill = BankAccount("Bill", 1000, 100)
bill.print_customer_information()
bill.deposit(500)
bill.withdraw(200)
bill.print_customer_information()
print('\n')
bob = BankAccount("Bob", 2000, 200)
bob.print_customer_information()
bob.withdraw(500)
bob.deposit(300)
bob.print_customer_information()
print('\n')
alice_checking = Checking("Alice", 1500, 100)
alice_checking.print_customer_information()
alice_checking.transfer_in(200)
alice_checking.transfer_out(100)
alice_checking.print_customer_information()
print('\n')
eve_savings = Savings("Eve", 3000, 500, 2.5)
eve_savings.print_customer_information()
eve_savings.apply_interest()
eve_savings.print_customer_information()
print('\n')
john_checking = Checking("John", 800, 50)
john_checking.print_customer_information()
john_checking.transfer_in(100)
john_checking.transfer_out(50)
john_checking.print_customer_information()
print('\n')
mary_savings = Savings("Mary", 5000, 1000, 3.0)
mary_savings.print_customer_information()
mary_savings.apply_interest()
mary_savings.print_customer_information()