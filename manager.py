class Manager(Person):
    def __init__(self, name, eid):
        Person.__init__(self, name)
        self.empID = eid

    def isEmployee(self):
        return True

    def getID(self):
        return self.empID
