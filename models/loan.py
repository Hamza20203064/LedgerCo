# borrower name
# bank name
# i
class Loan(object):
    def __init__(self):
        self.id = None
        self.borrower_name = None
        self.bank_name = None
        self.principal_amount = None
        self.interest_rate = None
        self.years = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setBorrowerName(self, borrower_name):
        self.borrower_name = borrower_name

    def getBorrowerName(self):
        return self.borrower_name

    def setBankName(self, bank_name):
        self.bank_name = bank_name

    def getBankName(self):
        return self.bank_name

    def setPrincipalAmount(self, principal_amount):
        self.principal_amount = principal_amount

    def getPrincipalAmount(self):
        return self.principal_amount
