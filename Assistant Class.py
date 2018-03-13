from Person Class.py import Person
from Account.py import Account

class Assistant(Person):
    def __init__(self, name, age, eid):
    	Person.__init__(self, name, age)
    	self.eid = eid  

    def isEmployee(self):
        return True  

    def view_balance(self, account):
    	Person.view_balance(self, account):

    def make_account(self, amount, account_name):
    	Person.make_account(self, amount, account_name)

    def get_name(self):
    	Person.get_name(self)

### Add specific functions only accesible by an Assistant (EMCAPSULATE)

