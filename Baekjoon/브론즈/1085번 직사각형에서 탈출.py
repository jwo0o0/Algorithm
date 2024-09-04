import sys
read = sys.stdin.readline

x, y, w, h = map(int, read().split())

# 각 경계선까지의 거리
distance = [x, y, w-x, h-y]

# 최솟값 찾기
min = 1000
for d in distance:
    if d < min: min = d

print(min)