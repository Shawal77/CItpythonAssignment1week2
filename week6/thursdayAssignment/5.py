class Person:
    def __init__(self,name: str,age: int,address: str) -> None:
        self.name=name
        self.age=age
        self.addr=address
    def eat(self,food: str=''):
        print(f'{self.name} is eating {food}')
    def sleep(self):
        print(f'{self.name} is sleeping')
    def work(self):
        print(f'{self.name} is working')
        
p1=Person('Shawal',29,'Makerere')
p1.eat()
p1.eat('matooke')
p1.sleep()
p1.work()
    
        