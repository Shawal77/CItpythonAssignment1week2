class Animal:
    def __init__(self) -> None:
        pass
class Dog(Animal):
    def __init__(self,name: str) -> None:
        super().__init__()
        self.name=name
    def bark(self):
        print(f'{self.name} is barking')

d1=Dog('Fred')
d1.bark()