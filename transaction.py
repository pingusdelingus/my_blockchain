class Transaction:
    def __init__(self,sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def getAmount(self):
        return self.amount