class Person:
    def __init__(
        self,
        f_name: str,
        l_name: str,
        age: int
    ) -> None:
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    def m1():pass
    def m2():pass
    
class Student(Person):
    def __init__(
        self, 
        f_name: str, 
        l_name: str, 
        age: int,
        course: str='Unspecified',
        university: str='Unspecified',
        year: int=0
    ) -> None:
        super().__init__(f_name, l_name, age)
        self.course=course
        self.university=university
        self.year=year
    def m1():pass
    def m2():pass