

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
    def __str__(self) -> str:
        return f'The account {self.accountNo} belongs to {self.owner}'
    def __repr__(self) -> str:
        return f'BankAccount{self.accountNo,self.balance,self.owner,self.type}'

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

class Bank():
    def __init__(
        self,
        bankName: str,
        accounts: list[BankAccount]
    ) -> None:
        self.name = bankName
        self.accounts = accounts
    def __repr__(self) -> str:
        return f'Bank{self.name,self.accounts}'
    def __str__(self) -> str:
        return f'This bank is called {self.name}'
    def addAccount(self,account: BankAccount):
        self.accounts.append(account)

    def addTransaction(self,tct: Transactions):
        for bAccount in self.accounts:
            if int(bAccount.accountNo) == int(tct.account.accountNo):
                bAccount.balance -= tct.amount
                print(f'Dear {bAccount.owner}, {tct.amount} was deduced from your account {bAccount.accountNo}.\n your new balance is {bAccount.balance}')
            else: print('Exitted if statement')
        else: print('Exiteed for loop')

class Customer:
    def __init__(
        self,
        customerName: str,
        accounts: list[BankAccount]
    ) -> None:
        self.name=customerName
        self.accounts=accounts
    def __str__(self) -> str:
        return f'This is {self.name} bank customer with {len(self.accounts)} accounts'
    def __repr__(self) -> str:
        return f'Customer{self.name,self.accounts}'
    def addAccount(self,account: BankAccount):
        self.accounts.append(account)

def main():
    #creating bank
    Rt6Bank=Bank(accounts=[],bankName = 'Rt6')
    #creating customer
    Shawal = Customer(customerName='Shawal',accounts=[])
    #creating bank account
    accShawal = BankAccount(
        accountNo='789655369',
        balance=7896451.24,
        owner='Shawal',
        type='savings'
    )
    #adding account to customer
    Shawal.addAccount(accShawal)
    #adding account to bank
    Rt6Bank.addAccount(account=accShawal)

    print('\n',Rt6Bank)
    print(repr(Rt6Bank))

    print('\n',Shawal)
    print(repr(Shawal))

    print('\n',accShawal)
    print(repr(accShawal),'\n')

    firstTrans = Transactions(
        account = accShawal,
        amount=1000.25,
        type='Acc to Wallet'
    )
    print('\n','Before transaction')
    print('\n',accShawal.balance)
    Rt6Bank.addTransaction(firstTrans)

    print('After transaction')
    print('\n',accShawal.balance)

if __name__=='__main__':
    main()







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


