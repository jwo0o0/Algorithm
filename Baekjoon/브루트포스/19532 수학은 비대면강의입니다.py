import sys
read = sys.stdin.readline

a, b, c, d, e, f = map(int, read().split())

# 최대 2000 * 2000 = 4000000 연산이므로 브루트포스 가능
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break