# Interface
# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

import abc  # abstract base class


class BalanceServiceInterface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def addBalance(self, balance, bank_name, bprrpwer_name, emi_no):
        pass
