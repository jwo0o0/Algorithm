import sys, heapq
read = sys.stdin.readline

N = int(read())

heap = [] # 최소 힙
result = [] # 결과를 저장할 배열
for _ in range(N):
    x = int(read())
    if (x == 0 and heap):
        result.append(heapq.heappop(heap))
    elif (x == 0 and not heap): # x가 0인데 배열이 비어있는 경우
        result.append(0)
    else: 
        heapq.heappush(heap, x)

for r in result:
    print(r)