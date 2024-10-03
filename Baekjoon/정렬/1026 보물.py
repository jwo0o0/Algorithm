import sys, heapq
read = sys.stdin.readline

N = int(read())

A = sorted(list(map(int, read().split())), reverse=True) # 내림차순 정렬
B = list(map(int, read().split())) # 최소 힙
heapq.heapify(B)

S = 0
for i in range(N):
    # A의 최댓값 * B의 최솟값
    S += A[i] * heapq.heappop(B)
print(S)

