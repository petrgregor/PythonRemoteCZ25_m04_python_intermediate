from abc import ABC, abstractmethod


class CreditCard(ABC):
    number = ""
    expiry = ""
    holder = ""

    @abstractmethod
    def pay(self):
        pass


class MasterCard(CreditCard):
    def __init__(self, number, expiry, holder):
        self.number = number
        self.expiry = expiry
        self.holder = holder

    def pay(self):
        print(f"Platím kartou MasterCard s číslem {self.number}")


class VisaCard(CreditCard):
    def __init__(self, number, expiry, holder):
        self.number = number
        self.expiry = expiry
        self.holder = holder

    def pay(self):
        print(f"Platím kartou Visa s číslem {self.number}")


if __name__ == "__main__":
    # credit_card = CreditCard()  # TypeError: Can't instantiate abstract class CreditCard without an implementation for abstract method 'pay'
    master_card = MasterCard(123456789, "10/2025", "Martin Novák")
    print(master_card)
    master_card.pay()

    visa_card = VisaCard(111222333, "11/2027", "Rudolf Jelínek")
    visa_card.pay()

    visa_card2 = VisaCard(789456132, "09/2026", "Jarda Svoboda")
    visa_card2.pay()
