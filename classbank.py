class bank_account:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance

    def display(self):
        print("account number=", self.acc_number)
        print("balance=", self.balance)

    def deposite(self, deposite_amount):
        self.deposite_amount = deposite_amount
        self.balance = self.deposite_amount+self.balance
        print("deposite amount=", self.deposite_amount)
        print("new amount=", self.balance)

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        self.balance = self.balance-self.withdraw_amount
        print("withdraw amount=", self.withdraw_amount)

    def check_balance(self):
        print("available balance=", self.balance)


obj1 = bank_account(55545899, 300)
obj1.display()
obj1.deposite(300)
obj1.withdraw(40)
obj1.check_balance()
