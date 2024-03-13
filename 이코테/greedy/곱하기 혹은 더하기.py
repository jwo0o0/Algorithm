# 곱하기 혹은 더하기

# 방법 1
# numbers = list(map(int, input()))

# count = numbers[0]
# for i in range(1, len(numbers)):
#     if (count * numbers[i] >= count + numbers[i]):
#         count *= numbers[i]
#     else:
#         count += numbers[i]
        
# print(count)

# 방법 2
data = input()
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중 하나라도 0 또는 1인경우 곱하기보다 더하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else: 
        result *= num
print(result)