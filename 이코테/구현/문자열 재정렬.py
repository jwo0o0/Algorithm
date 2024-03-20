data = input()
result = []
value = 0
for x in data:
    # 알파벳인 경우
    if x.isalpha():
        result.append(x)
    # 숫자인 경우
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))