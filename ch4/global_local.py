# 전역 변수 하나를 만들어보자. 클래스나 함수 내부에 속해있지 않은 모든 변수는 전역 변수이다
animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


# 함수에서 전역변수에 접근할려면?
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


# 함수에서 지역 변수
def change_local():
    animal = 'wombat'
    print('locals:', locals())

print(animal)
change_local()
print(globals())
