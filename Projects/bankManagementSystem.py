class Account:
    def __init__(self, acc, bal = 0):
        self.acc = acc
        self.bal = bal

    def deposit(self, amount):
        print("Amount Deposited: ", amount)
        self.bal += amount
        print("New Balance: ", self.bal)

    def withdraw(self, amount):
        print("Amount Withdrawn: ", amount)
        self.bal -= amount
        print("New Balance: ", self.bal)

    def getBal(self):
        print("Total Balance: ", self.bal)

    def getAcc(self):
        print("Account Number: ", self.acc)
acc1 = Account(39239939, 100)

acc1.deposit(100000)
acc1.withdraw(50000)
acc1.getAcc()
acc1.getBal()