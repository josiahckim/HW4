class Customer(Person):
  __accountList = []
  __accountCount = 0

  def __init__(self, name, age, eid, cashOnHand):
    Person.__init__(name, age, eid)
    self.cashOnHand = cashOnHand
  
  def makeAccount(self, initBalance, fee = 0, accnt_min = 0):
    if self.age < 16:
      print("You are too young to create an account!")
      return
    
    accountList.append(Account.__init__(initBalance, self.eid, str(self.eid) + "." + str(accountCount), fee, accnt_min))
    
  	def request_loan(self, amount):
		  self.debt = amount

	  def pay_loan(self, amount):
		  self.debt -= amount
    
