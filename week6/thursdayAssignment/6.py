class Employee:
    def __init__(
        self,
        name: str,
        age: int,
        salary: int,
    ) -> None:
        self.name=name
        self.age=age
        self.salary=salary
    def eat(self,food: str=''):
        print(f'{self.name} is eating {food}')
    def sleep(self):
        print(f'{self.name} is sleeping')
    def work(self):
        print(f'{self.name} is working')
class Programmer(Employee):
    def __init__(self, name: str, age: int, salary: int, plang: str='') -> None:
        super(Programmer, self).__init__(name, age, salary)
        self.name=name
        self.age=age
        self.salary=salary
        self.plang=plang
    def code(self):
        print(f'{self.name} is coding in {self.plang}')

shawal=Programmer('Shawal',19,2_000_000,'python')
shawal.eat()
shawal.sleep()
shawal.work()
shawal.code()