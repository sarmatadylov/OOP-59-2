from locale import currency


class Money:

    def __init__(self, amount, currnecy):
        self.amount = amount
        self.currency = currency


    def __add__(self, other):
        print(self.currency )

SOM = Money(100, "SOM")
USD = Money(100, "USD")

































