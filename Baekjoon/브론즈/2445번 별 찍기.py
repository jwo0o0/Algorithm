import sys
read = sys.stdin.readline

N = int(read())

# 별의 윗부분
for i in range(1, N + 1):
    print("*" * i + " " * (N-i) * 2 +"*" * i)
# 별의 아랫부분
for i in range(1, N):
    print("*" * (N-i) + " " * i + " " * i + "*" * (N-i))