# 일반적인 index를 활용한 for문 예시
total = 0
for i in range(1, 11, 2):
    total += (i + 1)
print(total)

# list comprehension
numbers = [number for number in range(1, 31)]
print(numbers)

even = [number for number in range(1, 51) if number % 2 == 0]
print(even)

a = range(3)
b = range(5)

# 2중 for 문 역할
for i in a:
    for j in b:
        print(i, j)

# tuple로 만들어서 list에 넣기
table = [(row, col) for row in a for col in b]
for space in table:
    print(space)

# tuple unpacking
for row, col in table:
    print(row, col)

# dictionary comprehension
word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# set comprehension
even_number_set = {number for number in range(1, 51) if number % 2 == 0}
print(even_number_set)

# generation comprehension
number_thing = (number for number in range(1, 11))
print(number_thing)
print(type(number_thing))
for number in number_thing:
    print(number)
