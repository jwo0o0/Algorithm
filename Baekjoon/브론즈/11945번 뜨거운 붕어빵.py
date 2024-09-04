import sys
read = sys.stdin.readline

N, M = map(int, input().split())

arr = [read().strip() for _ in range(N)]
# 문자열 슬라이싱으로 역순 출력
for a in arr:
    print(a[::-1])