import numbers


class CreditCard:
    def __init__(self,number,date,code) -> None:
        self.number=number
        self.exp_date=date 
        self.sec_code=code
    def display_card(self) -> None:
        print(f"""
              card number {self.number}
              expiration {self.exp_date}
              security code {self.sec_code}
              """)
my_cc=CreditCard(
    4489_3453_2434_2345,
    '23/12/2026',
    456
)
my_cc.display_card()