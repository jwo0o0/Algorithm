import sys
read = sys.stdin.readline

N = int(read())

# 재귀 -> 시간초과 
cnt = 0
def fib(n):
    global cnt
    if (n == 1 or n ==2):
        cnt += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# DP
f = [0] * (N+1)
def fibonacci(n):
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n];

print(fibonacci(N), N-2)
