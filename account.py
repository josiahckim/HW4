class Account:
  def __init__(self, balance, holderID, accountID, fees, account_min = 0):
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
  
  def makeDeposit(self, amount):
    self.balance += amount
  
  def makeWithdrawal(self, amount, isATM):
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
