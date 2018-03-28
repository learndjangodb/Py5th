# 1) Write a Program Create a class Named "Account" with initial parameters (name, accnum, balance), 
# and with four methods named (transfer_to_account, deposit, withdraw, display_balance).

class Account:
	def __init__(self, name, accnum, balance):
		self.name = name
		self.accnum = accnum
		self.balance = balance

	def transfer_to_account(self, account, amount):
		self.balance -= amount
		account.balance += amount

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def display_balance(self):
		print(self.balance)


ac1 = Account("ram", 123, 100)

ac1.deposit(100)

# ac1.display_balance()

ac2 = Account("kiran", 245, 200)

ac1.transfer_to_account(ac2, 100)

ac1.display_balance()
ac2.display_balance()

