import sys, math
read = sys.stdin.readline

H, W, N, M = map(int, read().split())
# H행 W열 좌석
# 세로 N칸 또는 가로 M칸 이상 비우고 앉아야 함 -> 최대 몇명?

w = math.ceil(W / (M + 1))
h = math.ceil(H / (N + 1))

print(w * h)