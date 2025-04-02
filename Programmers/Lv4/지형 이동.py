from collections import deque
from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    N = len(land)
    visited = [[False] * N for _ in range(N)]
    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = []
    heappush(queue, [0, 0, 0]) # [비용, i, j]
    while queue:
        cost, x, y = heappop(queue)
        if not visited[x][y]:
            visited[x][y] = True
            answer += cost
            for dx, dy in dt:
                nx, ny = x + dx, y + dy
                if nx in range(N) and ny in range(N):
                    diff = abs(land[x][y] - land[nx][ny])
                    if diff > height:
                        new_cost = diff
                    else:
                        new_cost = 0
                    heappush(queue, [new_cost, nx, ny])

    return answer