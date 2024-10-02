import sys, heapq
read = sys.stdin.readline

T = int(read())
result = []
for _ in range(T):
    input()
    N, M = map(int, read().split())
    sejun = list(map(int, read().split()))
    sebi = list(map(int, read().split()))
    # 최소 힙으로 정렬
    heapq.heapify(sejun)
    heapq.heapify(sebi)
    # 둘 다 원소가 있는 경우
    while sejun and sebi:
        if sejun[0] >= sebi[0]:
            heapq.heappop(sebi)
        elif sejun[0] < sebi[0]:
            heapq.heappop(sejun)

    if sejun:
        result.append('S')
    elif sebi:
        result.append('B')
    else:
        result.append('C')

for r in result: print(r)
    
    