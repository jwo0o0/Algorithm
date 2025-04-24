import sys
read = sys.stdin.readline

DIVIDE = 1_000_000_009

T = int(read())
case = []
for _ in range(T):
    case.append(int(read()))
    
dp = [1, 2, 4]
for i in range(3, max(case)):
    dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % DIVIDE)

for n in case:
    print(dp[n - 1])