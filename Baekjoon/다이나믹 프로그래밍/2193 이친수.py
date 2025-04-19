import sys
read = sys.stdin.readline

N = int(read())
memo = [0, 1, 1]
for i in range(3, N + 1):
    memo.append(memo[i-1] + memo[i-2])

print(memo[N])