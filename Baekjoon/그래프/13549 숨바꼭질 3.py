import sys
from collections import deque
read = sys.stdin.readline

MAX = 100001
N, K = map(int, read().split())

visited = [False] * MAX
visited[N] = True
dist = [0] * MAX
queue = deque([N])

while queue:
    current = queue.popleft()
    if current == K: break
    if (current * 2) in range(MAX) and not visited[current * 2]:
        queue.append(current * 2)
        dist[current * 2] = dist[current]
        visited[current * 2] = True
    if current - 1 in range(MAX) and not visited[current - 1]:
        queue.append(current - 1)
        dist[current - 1] = dist[current] + 1
        visited[current - 1] = True
    if current + 1 in range(MAX) and not visited[current + 1]:
        queue.append(current + 1)
        dist[current + 1] = dist[current] + 1
        visited[current + 1] = True

print(dist[K])