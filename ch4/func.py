# 위치인자
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 다음과 같이 dictionary가 만들어진다
a = menu('chardonnay', 'chicken', 'cake')
print(a)

# 하지만 순서가 이상하다면...???
a = menu('beef', 'bagel', 'bordeaux')
print(a)

# 키워드 지정 가능(키워드 인자)
a = menu(entree='beef', dessert='bagel', wine='bordeaux')
print(a)


# 파라메터 지정
def timetable(first, second, third='Mathematics'):
    return {
        '1st period': first,
        '2nd period': second,
        '3rd period': third
    }

my_table = timetable('English', 'Computer science')
print(my_table)

# 기본인자에 값을 넣는다면?
my_table = timetable('English', 'Computer science', 'Physics')
print(my_table)


# 기본인자로 리스트를 쓸때 주의할점!
def foo(arg, result=[]):
    result.append(arg)
    print(result)

foo(3)  # [3]
foo(4)  # [3, 4]


def bar(arg):
    result = list()
    result.append(arg)
    print(result)

bar(3)  # [3]
bar(4)  # [4]


def print_args(*args):
    """
    *의 사용법(포인터 아님)
    인자들을 튜플로 묶어버린다
    """
    print('Positional argument tuple: ', args)

print_args(1, 4, 5, 4, 3)


def multi_args(arg1, arg2, *args):
    """
    눈치챘겠지만 가변 인자로도 쓸수있다.
    """
    print("arg1 :", arg1)
    print("arg2 :", arg2)
    print("rest :", args)

multi_args('foo', 'bar', 'go', 'hang', 'a', 'salami', "i'm", 'a', 'lasagna', 'hog')


def keyword_args(**kwargs):
    """
    키워드 인자를 dictionary로 묶을때 이중 ** 사용.
    """
    print('Keyword arguments :', kwargs)
keyword_args(spain='estrella-dahm', france='blanc', belgium='stella artois')
print()

# docstring을 출력해보자
# docstring이란? 함수 내부에 3중 쌍따옴표로 된, 함수 정의에 문서를 붙인 것
help(print_args)
help(multi_args)
help(keyword_args)

print(print_args.__doc__)


def edit_story(words, func):
    """
    람다 표현을 적용해봅시다. func 에는 어떤 함수도 들어올 수 있다.
    """
    for word in words:
        print(func(word))


def exclamation_point(word):
    """
    단어 끝에 느낌표를 붙이는 함수
    """
    return word + '!'

day_of_week = ['monday', 'tuesday', 'wednesday']
edit_story(day_of_week, exclamation_point)


def piglatin(word):
    """
    :param word: word that would be changed into piglatin
    :return: piglatin version of word
    """
    return word[1:] + word[0] + 'ay'

print(piglatin('python'))


#데코레이터 함수란 서식함수
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


# 함수에 데코레이터를 수동으로 붙이는 형식
def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
res = cooler_add_ints(3, 5)
print(res)


# 함수에 자동으로 데코레이터를 붙이고 싶다면
@document_it
@square_it
def sub_ints(a, b):
    return a - b


print()
res = sub_ints(b=3, a=12)
print('res:', res)
print()


def add_two(a, b):
    return a + b

