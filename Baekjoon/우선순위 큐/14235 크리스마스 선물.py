import sys, heapq
read = sys.stdin.readline

n = int(read())
presents = [] # 현재 가진 선물을 저장하는 최대 힙
worth = [] # 아이들에게 준 선물의 가치
for _ in range(n):
    a = list(map(int, read().split()))
    # 아이들을 만난 경우
    if (a[0] == 0):
        # 선물이 있는 경우 가장 가치가 큰 선물 pop
        if (presents): worth.append(-heapq.heappop(presents))
        # 선물이 없는 경우 -1
        else: worth.append(-1)
    # 선물을 충전한 경우
    else:
        # 선물의 가치를 최대 힙에 push
        for present in a[1:]:
            heapq.heappush(presents, -present)

for w in worth:
    print(w)