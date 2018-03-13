class Account:
  __balance = 0
  __accountID = 0
  __holderID = 0
  
  def __init__(self, balance, holderID, accountID, fees = 0, account_min = 0):
    self.balance = balance
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
