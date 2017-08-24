import math


class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Circle with radius=%f, area=%f, perimeter=%f' % (self.radius, self.area, self.perimeter)

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @property
    def info(self):
        return dict({
            'diameter': self.diameter,
            'area': self.area,
            'perimeter': self.perimeter
        })

c = Circle(5)
print(c)
c.radius = 14
print(c)
print(c.info)
