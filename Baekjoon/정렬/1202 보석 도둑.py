import sys, heapq
read = sys.stdin.readline 

N, K = map(int, read().split())
# 보석의 [ 무게, 가격 ]
jewels = sorted([list(map(int, read().split())) for _ in range(N)]) 
# 각 가방의 최대 무게 
bags = sorted([int(read()) for _ in range(K)])

sum = 0
# 각 가방별로 훔칠 수 있는 보석을 최대 힙으로 탐색
    # 남은 보석이 있고, 가방에 첫번째 보석을 담을 수 있으면 최대 힙에 push
    # 가방에 담을 수 있는 보석이 있다면 최대 가격인 보석을 훔친다
    # 어차피 다음 가방에 담을 수 있는 무게가 많으므로 tmp를 유지
tmp = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewels)[1]) # jewels가 정렬되어 있으므로 첫번째 원소 pop
    if tmp:
        sum -= heapq.heappop(tmp)
    
print(sum)
    