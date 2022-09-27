class Person:
    def __init__(
        self,
        f_name: str,
        l_name: str,
        age: int,
        nick_name: str='Unspecified'
    ) -> None:
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.__nick_name=nick_name
    def get_n_name(self)->str:
        return self.__nick_name
    def set_n_name(self, name: str)->None:
        self.__nick_name = name
    def print_name(self)->None:
        print(f' {self.f_name} {self.l_name} ')
class Student(Person):
    def __init__(
        self, 
        f_name: str, 
        l_name: str, 
        age: int=0,
        course: str='Unspecified',
        university: str='Unspecified',
        year: int=0
    ) -> None:
        super().__init__(f_name, l_name, age)
        self.course=course
        self.university=university
        self.year=year
    def __str__(self)->str:
        return f'My name is {self.f_name,self.l_name} a {self.age} year old student at {self.university} persuing {self.course} year {self.year}'

shawal=Student(
    f_name='Shawal',
    l_name='Mbalire',
    age=19,
    course='BELE',
    university='Makerere University',
    year=2
)
print('\n')
print(shawal)
print(shawal.get_n_name())
shawal.set_n_name('Chess_master')
print(shawal.get_n_name())
shawal.print_name()
print('\n')