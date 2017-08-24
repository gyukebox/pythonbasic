# dictionary는 key: value 형식
web_frameworks = {
    'python': 'django',
    'javascript': 'node.js',
    'golang': 'martini'
}
print(web_frameworks)

# key가 중복이면 value가 덮어씌워짐
# key가 중복이 아니면 새로운 key-value 쌍이 append 됨
web_frameworks['java'] = 'spring'
web_frameworks['javascript'] = 'react'
web_frameworks['golang'] = 'revel'
print(web_frameworks)

# del 을 활용하여 key-value 쌍을 삭제할수있다
del web_frameworks['java']
print(web_frameworks)

if 'c' in web_frameworks:
    print("we can use c in web programming")
else:
    print("it is hard to use c in web programming")

print(list(web_frameworks.keys()))    # key만 뽑아온다
print(list(web_frameworks.values()))  # value 만 뽑아온다
print(list(web_frameworks.items()))   # 둘 다 뽑아온다 ((key, value) 형식의 튜플)

web = web_frameworks.copy()
# web = web_frameworks
# 할당과 복사의 차이 : 할당 후 값을 바꾸면 둘 다 영향 있지만 복사 후 값을 바꾸면 하나는 영향이 없다!
web['golang'] = 'beego'
print(web_frameworks)
print(web)
