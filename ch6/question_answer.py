# 1
class Thing:
    pass

print(Thing)
example = Thing()
print(example)


# 2
class Thing2:
    letters = 'abc'

print(Thing2.letters)


# 3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'

print(Thing3().letters)
# print(Thing3.letters) - Error


# 4, 5, 6
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return '#%s %s : %s' % (self.__number, self.__symbol, self.__name)

lightest = Element('Hydrogen', 'H', 1)
el_dict = {
    'name': 'Iron',
    'symbol': 'Fe',
    'number': 26
}
element = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(element)
print(lightest)
