import sys, bisect
read = sys.stdin.readline

# 조건값 입력
T = int(read())
N = int(read())
A = list(map(int, read().split()))
M = int(read())
B = list(map(int, read().split()))

# A와 B의 부 배열의 합을 저장하는 리스트
A_SUM, B_SUM = [], []

# A의 부분 배열의 합 구하기 O(N^2)
for i in range(N):
    current_sum = 0
    for j in range(i, N):
        current_sum += A[j]
        A_SUM.append(current_sum)
# B의 부분 배열의 합 구하기 O(M^2)
for i in range(M):
    current_sum = 0
    for j in range(i, M):
        current_sum += B[j]
        B_SUM.append(current_sum)

# 이진 탐색을 위해 정렬
A_SUM.sort()
B_SUM.sort()

count = 0 # 가능한 경우의 수
# 이진 탐색으로 합이 T가 되는 값의 개수를 구함
# 이중 for문으로 모든 경우를 탐색하면 시간 초과
for i in range(len(A_SUM)):
    left = bisect.bisect_left(B_SUM, T-A_SUM[i])
    right = bisect.bisect_right(B_SUM, T-A_SUM[i])
    count += right - left

print(count)