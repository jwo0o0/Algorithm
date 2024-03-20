# 1이 될때까지
N, K = map(int, input().split())

# 방법 1
# count = 0
# while N != 1:
#     if (N % K == 0): N /= K
#     else: N -= 1
#     count += 1

# 방법 2
result = 0
while True:
    target = (N // K) * K # N이 K로 나누어 떨어지는 수가 될때까지 빼기
    result += (N - target)
    N = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    result += 1
    N //= K
    
result += (N - 1)
print(result)