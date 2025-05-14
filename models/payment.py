# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

class Payment(object):
    def __init__(self, bank_name, borrower_name, lump_sum_amount, emi_no):
        self.id = None
        self.bank_name = bank_name
        self.borrower_name = borrower_name
        self.lump_sum_amount = lump_sum_amount
        self.emi_no = emi_no

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setBankName(self, bank_name):
        self.bank_name = bank_name

    def getBankName(self):
        return self.bank_name

    def setBorrowerName(self, borrower_name):
        self.borrower_name = borrower_name

    def getBorrowerName(self):
        return self.borrower_name

    def setLumpSumAmount(self, lump_sum_amount):
        self.lump_sum_amount = lump_sum_amount

    def getLumpSumAmount(self):
        return self.lump_sum

    def setEmiNo(self, emi_no):
        self.emi_no = emi_no

    def getEmiNo(self):
        return self.emi_no
