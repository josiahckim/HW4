class Person:
	active_user = 0;

	def __init__(self, name, age, eid):
		self.name = name
		self.age = age
		self.eid = eid
		self.debt = 0
		self.account_list = []


	'''def deposit(self, account, amount):
		if(hasAccount(account)):
			Account.deposit(amount)
		else:
			print("You do not have access to this account")	

	def withdraw(self, account_name, amount):
		if(hasAccount(account_name)):
			Account.withdraw(amount)
		else:
			print("You do not have access to this account")	'''

	def transfer(self, account_name_1, account_name_2, amount):
		if(hasAccount): #If they own account 1
			Account.transfer(amount)
		else:
			print("You do not have access to this account")	

	'''def view_balance(self, account):
		if(hasAccount): #If they own account 1
			Account.view_account_balance(account)
		else:
			print("You do not have access to this account")	'''



	def make_account(self, amount, account_name):
		Account.__init__(amount, self.eid, account_name)
		self.account_list.append(account_name)

	def delete_account(self, account_name):
		if(hasAccount(account_name)): #If they own account
			account.delete()
		else:
			print("You do not have access to this account")			




	def request_loan(self, amount):
		self.debt = amount

	def pay_loan(self, amount):
		self.debt -= amount

	def list_accounts(self):
		for x in self.account_list
			print(x + " ")#print the accounts that the person has	

	def get_name(self):
		return self.name



	def has_account(self, account_name):
		if(account_name in self.account_list)
			return True
		else
			return False


	


