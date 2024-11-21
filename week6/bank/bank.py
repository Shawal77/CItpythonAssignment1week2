#line 161 iden or line 119


import sys
import os
import secrets
import hashlib
from unicodedata import name
import mysql.connector
import re
from time import sleep
from datetime import datetime

MINIMUM_ACC_AMOUNT = 20_000

class Bank:
    def __init__(self,name,phone,pin) -> None:
        self.name=name
        self.phone=phone
        self.pin=hashlib.sha256(pin.encode()).hexdigest()
        self.accountNumber=self.create_account_number()
        self.balance=0
        self.accountNumberLogin=''
        self.create_database()
    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd = '',
                database='RT6 bank'
            )
        except:
            raise mysql.connector.Error('Could not connect to database')

        c = conn.cursor()
        return conn,c
    def create_database(self) -> None:
        conn,c=self.connect_db()
        c.execute('''CREATE TABLE IF NOT EXISTS RT6bank(id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) phone VARCHCAR(10) pin VARCHAR(255) account_number VARCHAR(255) not null unique
        balance INT) ''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions(
            id INT PRIMARY KEY AUTO_INCREMENT,
            account_number VARCHAR(255) not null'
            transaction type VARCHAR(255) not null,
            amount INT not null,
            date DATETIME default CURRENT_TIMESTAMP
        )''')
        conn.commit()
        conn.close()
        print('Database created')
    def create_acount_number(self) -> str:
        account_number = 'AC'+\
            self.phone[-4:]+datetime.now().strftime('%Y%m%d')+\
            str(secrets.randbits(15))
        return account_number
    def create_account(self):
        conn,c=self.connect_db()
        sql = ('''
        INSERT INTO RT6bank(name, phone, pin, account_number, balance)
        VALUES(%s,%s,%s,%s,%s)
        ''')
        data = (self.name,self.phone,self.pin,self.accountNumber,self.balance)
        try:
            c.execute(sql,data)
            conn.commit()
            print(f'Account created \n Your account Number is {self.account_number}')
        except mysql.connector.Error as err:
            print(f'Error :{str(err)}')
            conn.rollback()
        finally:
            c.close()
            conn.close()
    def get_balance(self):
        conn,c=self.connect_db()
        c.execute('''
        SELECT balance FROM bank WHERE account_number = %s
        ''',(self.accountNumberLogin))
        data = c.fetchone()
        conn.close()
        return data[0]
    def check_balance(self):
        print(f'Your current bslsnce is: {str(self.get_balance())}')
    def update_database(self,t_type,amount):
        conn,c=self.connect_db()
        c.execute('''
        UPDATE RT6bank SET balance = %s WHERE account_number = %s
        ''',(self.balance,self.accountNumberLogin))
        c.execute('''
        INSERT INTO transactions(account_number, transaction_type,amount)
        VALUES(%s, %s ,%s)
        ''',(self.accountNumberLogin,t_type,amount))
        print('Database updated')
    def depoisit(self,amount):
        self.balance=self.get_balance()+amount
        self.update_database('deposit',amount)
        print('Deposit Succesful')
        self.check_balance()
    def withdraw(self,amount):
        if (self.balance-amount)>MINIMUM_ACC_AMOUNT:
            self.balance-=amount
            self.update_database('withdraw',amount)
            print(f'You have withdrawn UGX {str(amount)}')
        else:
            print('Insufficient Funds')
    def transfer(self,amount,account_number):
        if (self.balance-amount)>MINIMUM_ACC_AMOUNT:
            if self.transfer_to_account(account_number,amount):
                self.balance = self.get_balance() -amount
                self.update_database('transfer',amount)
                print(f'transfer succesful\nYou transferred {str(amount)} to {account_number}')
        else:
            print('Insufficient Funds')
    def transfer_to_account(self,account_number,amount):
        conn,c = self.connect_db()
        c.execute('''
        SELECT account_number,balance FROM bank WHERE account_number = %s
        ''',(self.accountNumber))
        data=c.fetchone()
        if data is None:
            print('Account number does not exist')
            return False
        else:
            if data[0] == self.accountNumberLogin:
                print(' cannot transfer to your account')
                return False
            else:
                c.execute('''
                UPDATE RT6bank SET balance = %s WHERE account_number = %s
                ''',data[1]+amount,account_number)
                conn.commit()
                conn.close()
                return True
    def login(self,account_number,pin):
        conn,c=self.connect_db()
        c.execute('''SELECT * RT6bank WHERE account_number = %s''',(account_number))
        data=c.fetchone()
        conn.close()
        if data is None:
            print('Account does not exist')
        else:
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            if hashed_pin == data[3]:
                self.accountNumberLogin=data[4]
                self.balance=data[5]
                print('login succesful')
                return True
            else:
                print('incorrect pin')
                return False
    def check_phone(phone_number):
        return re.match(r'^(077|078|076|070|075|074|075)\d{7}$',phone_number)

def main():
    print('Welcome to RT6 Bank')
    print('1.)Create account\n2.) Login\n3.)Exit')
    userinput=input('Enter your choice')

    if userinput == '1':
        name=input('Enter your name')
        phone=input('Enter your phone number: ')

        while not check_phone(phone):
            print('Invalid phone number')
            phone=input('Enter your phone number')
        pin = input('Enter your pin')
        if not name or not phone or not pin:
            print('cannot create account, All fiealds are required')
            sys.exit(-1)
        else:
            bank = Bank(name,phone,pin)
            bank.create_account()
    elif userinput == '2':
        pass
    elif userinput == '3':
        pass
if __name__=='__main__':
    main()
