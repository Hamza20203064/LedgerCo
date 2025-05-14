class Payment(object):
    def __init__(self, amount: float, date: str, method: str):
        self.amount = amount
        self.date = date
        self.method = method
