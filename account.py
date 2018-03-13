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
    return self.balance
  
  def makeDeposit(self, amount, personID):
    # checks the account holder against the accessor's ID
    if not(checkOwner(personID)):
      return
    self.balance += amount
  
  def makeWithdrawal(self, amount, isATM, personID):
    # checks the account holder against the accessor's ID
    if not(checkOwner(personID)):
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
    # checks if the person attempting to access the account is the account holder
    return self.holderID == personID
