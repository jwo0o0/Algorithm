import sys, heapq
read = sys.stdin.readline

T = int(read())
result = []
for _ in range(T):
    input()
    N, M = map(int, read().split())
    sejun = list(map(int, read().split()))
    sebi = list(map(int, read().split()))
    heapq.heapify(sejun)
    heapq.heapify(sebi)
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
    
    