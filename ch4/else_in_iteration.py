numbers = [1, 3, 5, 7, 9]
pos = 0

# 반복문에 else가 붙는경우 = break 호출 여부 확인 위함
while pos < len(numbers):
    number = numbers[pos]
    if number % 2 == 0:
        print("Found even number: ", number)
        break
    pos += 1
else:  # break 호출 X
    print("No even number found")

for number in numbers:
    if number % 2 == 0:
        print("Found even number: ", number)
        break
else:
    print("No even number found")
