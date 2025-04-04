import sys
from collections import defaultdict, deque
read = sys.stdin.readline

N, M = map(int, read().split())
island = defaultdict(list)
max_limit = 0

for _ in range(M):
    A, B, C = map(int, read().split())
    island[A].append((B, C))
    island[B].append((A, C))
    max_limit = max(max_limit, C) # 이분 탐색을 위해 가장 큰 중량 제한 저장
    
start, end = map(int, read().split())


# BFS: mid 무게로 이동 가능한가?
def can_go(mid):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for neighbor, weight in island[current]:
            if not visited[neighbor] and weight >= mid:
                visited[neighbor] = True
                queue.append(neighbor)
    return False

# 이분 탐색
left = 1
right = max_limit
result = 0

while left <= right:
    mid = (left + right) // 2
    if can_go(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)
