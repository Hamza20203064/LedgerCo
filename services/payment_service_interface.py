# Interface
# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

import abc  # abstract base class


class PaymentServiceInterface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def addPayment(self, bank_name, borrower_name, lump_sum_amount, emi_no):
        pass
