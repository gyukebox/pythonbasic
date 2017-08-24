class Person:
    def __init__(self, name):
        self.name = name

    def introduce_oneself(self):
        print('Hello, my name is', self.name)

    @staticmethod
    def wake_up(complain):
        print(complain)


class CollegeStudent(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def introduce_oneself(self):
        print(self.school, 'student', self.name)


p = Person('gildong')
p.introduce_oneself()

gyu = CollegeStudent('Byeong Gyu', 'Konkuk University')
gyu.introduce_oneself()
Person.wake_up("fuck my life it's monday")
