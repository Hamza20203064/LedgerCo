
# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT


from services.balance_service_interface import BalanceServiceInterface
from models.balance import Balance


class BalanceService(BalanceServiceInterface):
    # Dictionary to store bill details--> as I  am not using db.
    balanDetails = {}

    def addBalance(self, balance, bank_name, bprrpwer_name, emi_no):
        balance = Balance(balance, bank_name, bprrpwer_name, emi_no)
        balance.setId(id)
        balance.setBalance(balance)
        balance.setBankName(bank_name)
        balance.setBorrowerName(bprrpwer_name)
        balance.setEmiNo(emi_no)

        # Store the bill in the dictionary
        self.__class__.balanDetails[id] = balance

        return balance
