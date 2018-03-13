class Customer(Person):
  __accountList = []
  accountNum = 1

  def __init__(self, name, age, eid):
    Person.__init__(name, age, eid)
  
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
    
    accountList.append(Account.__init__(initBalance, self.eid, str(self.eid) + "." + str(accountCount), fee, accnt_min))
    accountCount +=1
    
  def deposit(self, amount, account):
  # function name: deposit
  #
  # parameters: amount - the amount being deposited (a float), account - the index of the account in the customer's list of accounts
  # description of function: This function deposits some money into the account being referenced.
    accountList[account].makeDeposit(amount, self.eid)
  
  def withdraw(self, amount, account):
  # function name: withdraw
  #
  # parameters: amount - the amount being deposited, account - the index of the account in the customer's list of accounts
  # description of function: This funtion withdraws some amount of money from the account at index account.
  #   This is done by calling the 

  	def request_loan(self, amount):
      self.debt = amount

    def pay_loan(self, amount):
      self.debt -= amount
