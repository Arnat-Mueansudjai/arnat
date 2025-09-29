class BankAccount:
    
    def __init__(self, account_number,name,balance):
        self.account_number = account_number
        self.balance = balance  
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def bankfees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        return self.balance
    
    def display(self):
        print(f"Account Number:{self.account_number}")
        print(f"Account Holder:{self.name}")
        print(f"Balance:{self.balance}")
       

account = BankAccount(1234,"Arnat",1000)
account.display()
account.deposit(500)
account.withdraw(200)
print(account.bankfees()) 
account.display()

#นาย อาณัต เหมือนสุดใจ รหัส 6730202556 