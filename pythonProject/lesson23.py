# Instance method

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"balance ga {amount} pul qo'shildi"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"balansingizdagi mablag' yetarli emas! {self.balance}"
        self.balance -= amount
        return f"balance dan {amount} pul yechildi"

    def balanceF(self):
       return f"Balansingiz: {self.balance}"

bankAcc = BankAccount()

bank_Deposit = (int(input("balansga pul qo'shish: ")))
print(bankAcc.deposit(bank_Deposit))
bank_Withdraw = (int(input("balance dan pul yechish: ")))
print(bankAcc.withdraw(bank_Withdraw))
print(bankAcc.balanceF())

class Dog:
    total_dogs = 4

    @classmethod
    def get_total_dogs(cls):
        return f"itlar soni: {cls.total_dogs} ta"

# animal = Dog()
# print(animal.get_total_dogs())

class Math:
    @staticmethod
    def multiplay(a, b):
        return f"a va b ning ko'paytmasi: {a * b}"

# print(Math.multiplay(10, 10))