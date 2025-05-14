# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

from services.payment_service_interface import PaymentServiceInterface
from models.payment import Payment


class PaymentService(PaymentServiceInterface):
    # Dictionary to store payment details--> as I  am not using db.
    paymentDetails = {}

    def addPayment(self, bank_name, borrower_name, lump_sum_amount, emi_no):
        payment = Payment()
        payment.setBankName(bank_name)
        payment.setBorrowerName(borrower_name)
        payment.setLumpSumAmount(lump_sum_amount)
        payment.setEmiNo(emi_no)

        # Store the bill in the dictionary
        self.__class__.paymentDetails[id] = payment

        return payment
