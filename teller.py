class Teller(Person):
    def __init__(self, name, age, eid):
    	Person.__init__(self, name, age)
    	self.eid = eid

    def view_balance(self, account):
    	Person.view_balance(self, account):

    def get_name(self):
    	Person.get_name(self)

