import random

class Person:
	active_user = 0
	current_eid = 0

	def __init__(self, name, age):
		self.name = name
		# if an invalid age is entered, we will asume the person is an infant
		if age < 0:
			age = 0
		self.age = age
		self.eid = str(Person.current_eid) + str(random.randint(100, 500))
		self.debt = 0
		self.account_list = []
		Person.current_eid += 1

	def delete_account(self, account_name):
		if(hasAccount(account_name)): #If they own account
			account.delete()
		else:
			print("You do not have access to this account")
			
	def displaySelf(self):
	# function name: displaySelf
	#
	# parameters: none
	# description of function: Displays the basic information about the person.
		print("Name:", self.name, "\tAge:", self.age)

	def get_name(self):
		return self.name



class Assistant(Person):
    def __init__(self, name, age):
    	Person.__init__(self, name, age)
			Manager.employeeList.append(self)


    def isEmployee(self):
        return True  

    def view_balance(self, account):
    	Person.view_balance(self, account)

    def make_account(self, amount, account_name):
    	Person.make_account(self, amount, account_name)
	
	def displaySelf(self):
	# function name: displaySelf
	#
	# parameters: none
	# description of function: Prints information about this assistant.
		print("Name:", self.name, "\tAge:", self.age, "\tRole: Assistant")





class Manager(Person):
	employeeList = []
	
  def __init__(self, name, age):
    Person.__init__(self, name, age)

  def viewCustomer(custom):
		custom.displaySelf()
	
	def displaySelf(self):
	# function name: displaySelf
	#
	# parameters: none
	# description of function: Prints information about this manager.
		print("Name:", self.name, "\tAge:", self.age, "\tRole: Manager")


  def deleteAccount():





class Teller(Person):
	def __init__(self, name, age):
		Person.__init__(self, name, age)  

  def isEmployee(self):
    return True  

  def view_balance(self, account):
    Person.view_balance(self, account)

	def get_name(self):
    Person.get_name(self)

	def displaySelf(self):
	# function name: displaySelf
	#
	# parameters: none
	# description of function: Prints information about this teller.
		print("Name:", self.name, "\tAge:", self.age, "\tRole: Teller")
	
	def makeTransfer(customer1, customer2, account1, account2, amount):
	# function name: makeTransfer
	#
	# parameters: customer1 - the customer funds are being transfered from, customer2 - the customer funds are being tranfered to,
	# 	account1 - the name of the account funds are being transfered from, account2 - the name of the account funds are being
	# 	transfered to, amount - the amount of money to be transfered
	# description of function: Transfer funds from customer1's account1 to customer2's account2. The amount to be transfered is given
	# 	by amount
	
		if customer1.balance(account1) < amount:
			print("insufficient funds in account:", account1)
		
		# ATM will be set to False here because the transfer is done by the teller, i.e. in the bank
		customer1.withdraw(account1, False, amount)
		customer2.deposit(account2, amount)





class Customer(Person):
  def __init__(self, name, age):
    Person.__init__(self, name, age)
    self.__accountList = []
		self.__accountNames = []
    self.accountNum = 1
  
  def getAccountList(self):
  # function name: getAccountList
  #
  # parameters: none
  # description of function: This function returns the values within the encapsulated variable accountList
    return self.__accountNames

  def printAccountList(self):
	# function name: printAccountList
	#
	# parameters: none
	# description of function: This function prints out a formated list of all accounts held by the customer.
	
	i = 1
  	for account in self.__accountList:
  		print("Account", str(i), account)
		i += 1
  
  def makeAccount(self, initBalance, fee = 0, accnt_min = 0):
  # function name: makeAccount
  #
  # parameters: initBalance - initial balance for the account, fee - ATM fee amount, 
  #   accnt_min - minimum required balance for the account
  # description of function: This function creates a new Account object 
    
    # Checks to ensure that only someone old enough to hold an account is creating the account
    if self.age < 16:
      print("You are too young to create an account!")
      return
    
    self.__accountList.append(Account(initBalance, self.eid, str(self.eid) + "." + str(self.accountNum), self.name, fee, accnt_min))
		self.__accountNames.append(str(self.eid) + "." + str(self.accountNum))
    self.accountNum +=1
		Account.listOfAccounts.append(self.__accountList[-1])
    
  def deposit(self, amount, account):
  # function name: deposit
  #
  # parameters: amount - the amount being deposited (a float), account - the index of the account in the customer's list of accounts
  # description of function: This function deposits some money into the account being referenced.
    self.__accountList[self.__accountNames.indexOf(account)].makeDeposit(amount, self.eid)
  
  def withdraw(self, amount, ATM, account):
  # function name: withdraw
  #
  # parameters: amount - the amount being deposited, account - the index of the account in the customer's list of accounts, 
  #   ATM - a boolean variable that is true if the transaction is occuring at an ATM.
  # description of function: This function withdraws some amount of money from the account at index account.
  #   This is done by calling the makeWithdrawal function for the referenced account.
    self.__accountList[self.__accountNames.indexOf(account)].makeWithdrawal(amount, ATM, self.eid)
	
	def balance(self, account):
	# function name: balance
	#
	# parameters: account - the name of the account funds will be withdrawn from
	# description of function: This function returns the balance of an account held by the customer.
	
		return self.__accountList[self.__accountNames.indexOf(account)].getBalance()

  def displaySelf(self):
  # function name: displayCustomer
  #
  # paramters: none
  # description of function: This function displays information about the customer.
	
		print("Name:", self.name, "\tAge:", self.age, "\tRole: Customer", "\nAccounts:")
		self.printAccountList()
		
  def get_loan(self):
  # function name: get_loan
  #
  # paramters: none
  # description of function: This function allows the customer to recieve a loan with a fixed, non-compounding interest rate.
    loan_request = float(input("Based on your balance, you can borrow any amount you want with an 8% interest rate. \nEnter the amount you wish to borrow:     
    self.debt += loan_request + (loan_request*.08)				 
    print("You are now ${} in debt".format(self.debt))
															 
			   
  def pay_loan(self):
  # function name: pay_loan
  #
  # paramters: none
  # description of function: This function allows the customer to pay a loan with their balance.
		account = input("Enter the account you want to make a payment from: ")
    balance = self.balance(self, account)
    pay = float(input("You are ${} in debt and your balance is ${}. \nEnter the amount you would like to pay: ".format(self.debt, balance)))
    while pay > balance and pay < 0:
        pay = float(input("You cannot make that payment. \nEnter a different amount: ")
    self.debt -= pay
    withdraw(self, pay, False, account)
    print("You are now ${} in debt and your balance is ${}.".format(self.debt, self.getBalance(self, account))) 	



class Account:
	listOfAccounts = []
	
  def __init__(self, balance, holderID, accountID, holderName, fees = 0, account_min = 0):
    self.__balance = float(balance)
    self.__holderID = holderID
    self.__accountID = accountID
    self.__holderName = holderName
    # in case the user enters an invalid minimum account value
    if account_min < 0:
      account_min = 0
    self.account_min = account_min
		if fees < 0:
			fees = 0
    self.fees = fees
	
	def displayAccounts():
	# function name: displayAccounts
	#
	# parameters: none
	# description of function: Prints a formatted list of all accounts
	
		i = 1
		for account in Account.listOfAccounts:
			print("Account", str(i) + ":", str(account))

  def getBalance(self):
  # function name: getBalance
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable balance for the current object being referenced.
    return self.__balance
  
  def getAccountID(self):
  # function name: getAccountID
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable accountID for the current object being referenced.
    return self.__accountID
    
  def getHolderID(self):
  # function name: getHolderID
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable holderID for the current object being referenced.
    return self.__holderID
	
	def getHolderName(self):
	# function name: getHolderName
	#
	# parameters: none
	# description of function: Returns the name of the account holder
		return self.__holderName
  
  def makeDeposit(self, amount, personID):
  # function name: makeDeposit
  #
  # parameters: amount - the amount being deposited, personID - the ID of the person making the deposit
  # description of function: This function increases the balance of the account object by amount. If the person making the 
  #   deposit is not the account holder, the function will exit after displaying that error message.
  
    # checks the account holder against the accessor's ID
    if not(Account.__checkOwner(self,personID)):
      print("You do not have permission to access this account!")
      return
    self.__balance += amount
  
  def makeWithdrawal(self, amount, isATM, personID):
  # function name: makeWithdrawal
  #
  # parameters: amount - the amount being withdrawn from the account, isATM - a boolean value that, if true, will add the fee
  #   amount to the withdrawal amount, personID - the ID of the person making the withdrawal
  # description of function: This function will withdraw the amount or amount plus fees if the isATM variable is False or True, 
  #   respectively. It also will check to make sure the final balance will not be below the account's minimum balance before.
  
    # checks the account holder against the accessor's ID
    if not(__checkOwner(personID)):
      print("You do not have permession to access this account!")
      return
    if isATM:
      # checking if the amount and ATM fee will reduce the account below its minimum
      if self.balance - amount - self.fees < self.account_min:
        print("insufficient funds")
      self.__balance -= fees
      self.__balance -= amount
    else:
      # checking if the amount will reduce the account below its minimum
      if self.__balance - amount < self.account_min:
        print("insufficient funds")
      self.__balance -= amount

  def __checkOwner(self, personID):
  # function name: checkOwner
  #
  # parameters: personID - the ID of the person accessing the class
  # description of function: This function is an encapsulated function that compares the Account object's variable holderID to 
  #   the passed in personID
  
    # checks if the person attempting to access the account is the account holder
    return self.__holderID == personID

  def __str__(self):
	# function name: __str__
	#
	# parameters: none
	# description of function: This function returns the account information formated as a string.
  	return "Account ID:" + self.__accountID + "\tHolderName:" + self.__holderName + "\n\tBalance:" + str(self.__balance)



#Test case

Bob = Customer("Bob", 20)
Bob.makeAccount(300, 0, 0)
Bob.deposit(30.3, 0)
Bob.printAccountList()
