# Interface
# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST

import abc  # abstract base class


class LoanServiceInterface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def addloan(self, bank_name, borrower_name, principal_amount, years, interest_rate):
        pass
