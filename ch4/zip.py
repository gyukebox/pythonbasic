english = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
spanish = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

# zip 활용하여 2개 이상의 iterable 순회 가능
for eng, esp in zip(english, spanish):
    print(eng, "=", esp)

# zip 사용하면 같은 인덱스의 원소들이 튜플로 묶임
# 튜플을 원소로 하여서 리스트를 만들수 있음
day_of_week = list(zip(english, spanish))
print(day_of_week)

# dict 사용하면 튜플이 언패킹되어서 key : value 형식으로 묶임
day_of_week_dict = dict(zip(english, spanish))
print(day_of_week_dict)
