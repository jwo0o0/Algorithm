import sys
read = sys.stdin.readline

MOD = 1_000_000_009

T = int(read())
case = []
for _ in range(T):
    case.append(int(read()))

memo = [[0, 0, 0] for _ in range(max(case) + 1)]
memo[1] = [1, 0, 0]
memo[2] = [0, 1, 0]
memo[3] = [1, 1, 1]
for i in range(4, max(case) + 1):
    memo[i][0] = (memo[i-1][1] + memo[i-1][2]) % MOD
    memo[i][1] = (memo[i-2][0] + memo[i-2][2]) % MOD
    memo[i][2] = (memo[i-3][0] + memo[i-3][1]) % MOD

for n in case:
    print(sum(memo[n]) % MOD)