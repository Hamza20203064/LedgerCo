# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST

from services.loan_service_interface import LoanServiceInterface
from models.loan import Loan


class LoanService(LoanServiceInterface):
    # Dictionary to store bill details--> as I  am not using db.
    loanDetails = {}

    def addloan(self, bank_name, borrower_name, principal_amount, years, interest_rate):
        loan = Loan()
        loan.setId(id)
        loan.setBankName(bank_name)
        loan.setBorrowerName(borrower_name)
        loan.setPrincipalAmount(principal_amount)
        loan.setYears(years)
        loan.setInterestRate(interest_rate)

        # Store the bill in the dictionary
        self.__class__.loanDetails[id] = loan

        return loan
