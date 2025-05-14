# Interface
import abc  # abstract base class


class LoanServiceInterface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def addloan(self, id, borrower_name, bank_name, principal_amount, years, interest_rate):
        pass
