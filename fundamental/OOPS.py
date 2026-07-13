#Q1
class BankAccount:
    
    def __init__(self , account_number , owner_name , balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def  deposit(self, amount):
        self.balance += amount 
        print(f"this new balance is {self.balance}")
        
    def withdraw(self ,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
        print(f"Remaining balance is {self.balance}") 
        
    def check_balance(self):
        print(f"the balance is {self.balance}")    
        
    def details(self):
        print(f"Name : {self.owner_name} and balance is {self.balance}")    
        
b1 = BankAccount(10,"Himesh Badlani",0)


