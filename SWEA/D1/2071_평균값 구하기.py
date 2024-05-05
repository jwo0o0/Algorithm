T = int(input())

result = []
for i in range(0, T):
    numbers = list(map(int, input().split()))
    sum = 0
    for num in numbers:
        sum += num
    result.append(round(sum / 10))

for i, avg in enumerate(result):
    print("#{} {}".format(i+1, avg))