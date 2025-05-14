from services.loan_service_interface import LoanServiceInterface
from models.loan import Loan


class LoanService(LoanServiceInterface):
    # Dictionary to store bill details--> as I  am not using db.
    loanDetails = {}

    def addLoan(self, id, name):
        user = Loan()
        user.setId(id)
        user.setName(name)

        self.__class__.userDetails[id] = loan
        return user
