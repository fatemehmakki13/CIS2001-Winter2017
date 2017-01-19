class BankAccount:
    
    def __init__(self,name,number):
        self._name = name
        self._number = number
        self._balance = 0

    def GetName(self):
        return self._name

    def GetNumber(self):
        return self._number

    def GetBalance(self):
        return self._balance

    def Withdraw(self, amount ):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError('Amount to withdraw exceeds balance')

    def Deposit(self, amount ):
        if amount >= 10000:
            print( 'Fatemeh has to do paperwork for us' )
        self._balance += amount

    def __add__(self, other):
        result = BankAccount(self.GetName() + "1", self.GetNumber() + 1 )
        result._balance = self.GetBalance() + other.GetBalance()
        return result

    def __str__(self):
        return "Name: " + self._name + " Number: " + str(self._number) + " Balance: " + str(self._balance)

checking = BankAccount("Eric's Checking", 123456789)
savings = BankAccount("Eric's Savings", 234567890)

checking.Deposit(1000)
savings.Deposit(2000)


new_account = checking + savings
# short hand for this
new_account = checking.__add__(savings)

print(checking)
print(new_account)
print(savings)
#checking = checking - savings

