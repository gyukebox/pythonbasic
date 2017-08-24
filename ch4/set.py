# 집합(set) 에는 순서가 없다!
# 아래 drinks는 key 당 value 가 set인 dictionary
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# 기본적으로 dictionary를 순회하면 key 값만 호출 가능
for name in drinks:
    print(name)

# 둘 다 꺼내오려면 items() 메소드를 사용해야함
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print()

for name, contents, in drinks.items():
    if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
        print(name)

print()

# & 연산자를 사용해서 코드를 간소화시킬수 있음
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print()

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

a = {1, 2}
b = {2, 3}

print(a & b)  # & : a와 b의 교집합
print(a | b)  # | : a와 b의 합집합
print(a - b)  # - : a에 대한 b의 차집합
print(a ^ b)  # ^ : a와 b의 교집합의 여집합(둘다 들어있는것만 아니면됨)

# 순서대로 &, |, -, ^ 에 해당됨(코드 해석은 직역!)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
