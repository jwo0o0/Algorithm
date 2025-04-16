import sys
read = sys.stdin.readline

N = int(read())
pack = list(map(int, read().split()))

price = [0] + pack
for i in range(2, N + 1):
    for j in range(i // 2 + 1):
        price[i] = max(price[i], price[j] + price[i-j])
        
print(price[N])