class BankAccount():
    def __init__(
        self,
        accountNo: str,
        balance: float,
        owner: str,
        type: str,
    ):
        self.accountNo = accountNo
        self.balance = balance
        self.owner = owner
        self.type = type
        
class Bank():
    def __init__(
        self,
        bankName: str,
        accounts: list[BankAccount]
    ) -> None:
        self.name = bankName
        self.accounts = accounts
        
class Customer:
    def __init__(
        self,
        customerName: str,
        accounts: list[BankAccount]        
    ) -> None:
        self.name=customerName
        self.accounts=accounts

class Transactions:
    def __init__(
        self,
        account: BankAccount,
        amount: float,
        type: str
    ):
        self.account = account
        self.amount = amount
        self.type = type
        
def main():
    Rt6Bank=Bank(accounts=[],name='Rt6')
    Shawal = Customer(customerName='Shawal',accounts=[])
    accShawal = BankAccount(
        accountNo='789655369',
        balance=7896451.24,
        owner='Shawal',
        type='savings'
    )
    print(Rt6Bank)
    print(Shawal)
    print(accShawal)
    firstTrans = Transactions(
        BankAccount = '789655369'
        amount=1000.25
        type='Acc to Wallet'
    )
    



    





'''Using classes, Create a basic banking application with the following features:

Create a class called BankAccount with the following attributes:

account_number - a string
balance - a float
owner - a string
type - a string
Create a class called Bank with the following attributes:

name - a string
accounts - a list of BankAccount objects
Create a class called Customer with the following attributes:

name - a string
accounts - a list of BankAccount objects
Create a class called Transactions with the following attributes:

 1. `account` - a `BankAccount` object
 2. `amount` - a float
 3. `type` - a string
The application should have the following functionality:

Create a new Bank object
Create a new Customer object
Create a new BankAccount object
Add the BankAccount object to the Bank object
Add the BankAccount object to the Customer object
Print the Bank object
Print the Customer object
Print the BankAccount object
Create a new Transaction object
Add the Transaction object to the BankAccount object'''


