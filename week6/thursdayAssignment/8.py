class Animal:
    def __init__(self,name,color,age) -> None:
        self.name=name
        self.color=color
        self.age=age
    def eat(self):
        print(f' {self.name} is eating')
    def sleep(self):
        print(f' {self.name} is sleeping')
    def make_sound(self):
        print(f' {self.name} is making sound')
class Dog(Animal):
    def __init__(self,name,color,age,breed) -> None:
        super().__init__(name,color,age)
        self.breed=breed
    def bark(self):
        print(f'{self.name} {self.breed} is barking')

d1=Dog('Fred','Blue',4,'UG')
d1.bark()