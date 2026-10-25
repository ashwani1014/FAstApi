class BankAccount:
    def __init__(self,balance:float =0 ):
        if balance <0 :
            raise ValueError("Balance can not be negative")
        self.__balance = balance

    @property
    def balance (self)-> float:
        return self.__balance

    def deposit (self,amount:float)->None:
        if amount <=0:
              raise ValueError("Deposit amount must be positive")  
        self.__balance +=amount  

    def withdraw (self,amount:float)->None:
        if amount <=0:
             raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -=amount  

account=BankAccount(10000)
print("creating a bank account")
print(account.balance)
account.deposit(20000)
print(account.balance)
account.withdraw(10000)
print(f"Final balance : {account.balance}") 