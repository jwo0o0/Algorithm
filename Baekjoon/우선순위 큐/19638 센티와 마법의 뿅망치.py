import sys, heapq
read = sys.stdin.readline

N, H, T = map(int, read().split())

# 거인들의 키를 저장할 최대 힙
heights = []
for _ in range(N):
    # 각 거인의 키를 최대 힙에 push
    heapq.heappush(heights, -int(read()))

count = 0
# 뿅망치의 횟수 제한만큼
for _ in range(T):
    # 가장 큰 거인의 키를 확인
    # pop했으므로 다시 push
    max_height = -heights[0]
    # 센티의 키 > 가장 큰 거인의 키 OR 가장 큰 거인의 키가 1인 경우 break
    if (H > max_height or max_height == 1):
        break
    # 뿅망치를 한 번 사용
    # 예외) 가장 큰 키가 1인 경우 그대로 다시 push
    count += 1
    max_height = -heapq.heappop(heights)
    if (max_height == 1):  heapq.heappush(heights, -max_height)
    else: heapq.heappush(heights, -int(max_height / 2))


# 가장 큰 거인의 키  
max_height = -heapq.heappop(heights)
print(f'YES\n{count}' if H > max_height else f'NO\n{max_height}')