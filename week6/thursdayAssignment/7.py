class Vehicle:
    def __init__(self,make,model,year) -> None:
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print(f'{self.make} {self.model} {self.year} is starting')
    def stop(self):
        print(f'{self.make} {self.model} {self.year} is stoping')
    def drive(self):
        print(f'{self.make} {self.model} {self.year} is driving')
        
class Car(Vehicle):
    def __init__(self, make, model, year,color) -> None:
        super().__init__(make, model, year)
        self.color=color
    def park(self):
        print(f'{self.make} {self.model} {self.year} {self.color} is parking')

c1=Car('Ferrari','one','2022','black')
c1.start()
c1.drive()
c1.park()
c1.stop()