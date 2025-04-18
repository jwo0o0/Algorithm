import sys
read = sys.stdin.readline

N = int(read())
pack = list(map(int, read().split()))

min_price = [0] + pack
for i in range(2, N + 1):
    for j in range(i // 2 + 1):
        min_price[i] = min(min_price[i], min_price[j] + min_price[i-j])

print(min_price[N])