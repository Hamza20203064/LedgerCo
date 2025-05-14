# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

class Balance(object):
    def __init__(self, balance: float, bank_name: str, borrower_name: str, emi_no: int):
        self.id = None
        self.balance = balance
        self.bank_name = bank_name
        self.borrower_name = borrower_name
        self.emi_no = emi_no
        self.amount_paid = 0
        self.no_of_emis_left = 0
        self.total_amount = 0

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setBalance(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def setBankName(self, bank_name):
        self.bank_name = bank_name

    def getBankName(self):
        return self.bank_name

    def setBorrowerName(self, borrower_name):
        self.borrower_name = borrower_name

    def getBorrowerName(self):
        return self.borrower_name

    def setEmiNo(self, emi_no):
        self.emi_no = emi_no

    def getEmiNo(self):
        return self.emi_no

    def setAmountPaid(self, amount_paid):
        self.amount_paid = amount_paid

    def getAmountPaid(self):
        return self.amount_paid

    def setNoOfEmisLeft(self, no_of_emis_left):
        self.no_of_emis_left = no_of_emis_left

    def getNoOfEmisLeft(self):
        return self.no_of_emis_left

    def setTotalAmount(self, total_amount):
        self.total_amount = total_amount

    def getTotalAmount(self):
        return self.total_amount

    def __str__(self):
        return f"Balance [bank_name={self.bank_name}, borrower_name={self.borrower_name}, bank_name={self.bank_name}, borrower_name={self.borrower_name}, amount_paid={self.amount_paid}, no_of_emis_left={self.no_of_emis_left}]"
