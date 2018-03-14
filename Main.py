import random

class Person:
	active_user = 0
	current_eid = 0

	def __init__(self, name, age):
		self.name = name
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


	#def list_accounts(self, c):
	#	for x in c.getAccountLists()
	#		print(x + " ")#print the accounts that the person has	




	def get_name(self):
		return self.name

'''	def view_balance(self, account):
		if(hasAccount): #If they own account 1
			Account.view_account_balance(account)
		else:
			print("You do not have access to this account")	'''



class Assistant(Person):
    def __init__(self, name, age):
    	Person.__init__(self, name, age)


    def isEmployee(self):
        return True  

    def view_balance(self, account):
    	Person.view_balance(self, account)

    def make_account(self, amount, account_name):
    	Person.make_account(self, amount, account_name)

    def get_name(self):
    	Person.get_name(self)

### Add specific functions only accesible by an Assistant (EMCAPSULATE)





class Manager(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def isEmployee(self):
        return True

    def getID(self):
        return self.empID



class Teller(Person):
    def __init__(self, name, age):
    	Person.__init__(self, name, age)  

    def isEmployee(self):
        return True  

    def view_balance(self, account):
    	Person.view_balance(self, account)

    def get_name(self):
    	Person.get_name(self)







class Customer(Person):
  __accountList = []
  accountNum = 1

  def __init__(self, name, age):
    Person.__init__(self, name, age)
  
  def getAccountList(self):
  # function name: getAccountList
  #
  # parameters: none
  # description of function: This function returns the values within the encapsulated variable accountList
    return self.accountList
  
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
    
    self.__accountList.append(Account.__init__('se',initBalance, self.eid, str(self.eid) + "." + str(self.accountNum), fee, accnt_min))
    self.accountNum +=1
    
  def deposit(self, amount, account):
  # function name: deposit
  #
  # parameters: amount - the amount being deposited (a float), account - the index of the account in the customer's list of accounts
  # description of function: This function deposits some money into the account being referenced.
    accountList[account].makeDeposit(amount, self.eid)
  
 # def withdraw(self, amount, account):
  # function name: withdraw
  #
  # parameters: amount - the amount being deposited, account - the index of the account in the customer's list of accounts
  # description of function: This funtion withdraws some amount of money from the account at index account.
  #   This is done by calling the 









class Account:

  
  def __init__(self, balance, holderID, accountID, fees = 0, account_min = 0):
    self.balance = 0
    self.holderID = holderID
    self.accountID = accountID
    # in case the user enters an invalid minimum account value
    if account_min < 0:
      account_min = 0
    self.account_min = account_min
    self.fees = fees

  def getBalance(self):
  # function name: getBalance
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable balance for the current object being referenced.
    return self.balance
  
  def getAccountID(self):
  # function name: getAccountID
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable accountID for the current object being referenced.
    return self.accountID
    
  def getHolderID(self):
  # function name: getHolderID
  #
  # parameters: none
  # description of function: Returns the value of the encapsulated variable holderID for the current object being referenced.
    return self.holderID
  
  def makeDeposit(self, amount, personID):
  # function name: makeDeposit
  #
  # parameters: amount - the amount being deposited, personID - the ID of the person making the deposit
  # description of function: This function increases the balance of the account object by amount. If the person making the 
  #   deposit is not the account holder, the function will exit after displaying that error message.
  
    # checks the account holder against the accessor's ID
    if not(checkOwner(personID)):
      print("You do not have permission to access this account!")
      return
    self.balance += amount
  
  def makeWithdrawal(self, amount, isATM, personID):
  # function name: makeWithdrawal
  #
  # parameters: amount - the amount being withdrawn from the account, isATM - a boolean value that, if true, will add the fee
  #   amount to the withdrawal amount, personID - the ID of the person making the withdrawal
  # description of function: This function will withdraw the amount or amount plus fees if the isATM variable is False or True, 
  #   respectively. It also will check to make sure the final balance will not be below the account's minimum balance before.
  
    # checks the account holder against the accessor's ID
    if not(checkOwner(personID)):
      print("You do not have permession to access this account!")
      return
    if isATM:
      # checking if the amount and ATM fee will reduce the account below its minimum
      if self.balance - amount - self.fees < self.account_min:
        print("insufficient funds")
      self.balance -= fees
      self.balance -= amount
    else:
      # checking if the amount will reduce the account below its minimum
      if self.balance - amount < self.account_min:
        print("insufficient funds")
      self.balance -= amount

  def __checkOwner(self, personID):
  # function name: checkOwner
  #
  # parameters: personID - the ID of the person accessing the class
  # description of function: This function is an encapsulated function that compares the Account object's variable holderID to 
  #   the passed in personID
  
    # checks if the person attempting to access the account is the account holder
    return self.holderID == personID
