# emi no.
# rate of interest
# emi amount
#

class Emi(object):
    def __init__(self):
        self.id = None
        self.rate_of_interest = None
        self.emi_amount = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setRateOfInterest(self, rate_of_interest):
        self.rate_of_interest = rate_of_interest

    def getRateOfInterest(self):
        return self.rate_of_interest

    def setEmiAmount(self, emi_amount):
        self.emi_amount = emi_amount

    def getEmiAmount(self):
        return self.emi_amount
