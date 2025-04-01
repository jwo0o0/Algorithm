import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())

# 수빈 현재 N, 동생 현재 K
# 수빈 X에서 X-1 or X+1 or 2*X
# 0 <= N, K <= 100,000

MAX = 100001
queue = deque([N])
visited = [False] * MAX
visited[N] = True
parent = [-1] * MAX
dist = [0] * MAX

while queue:
    current = queue.popleft()
    if current == K:
        break
    for next in (current - 1, current + 1, current * 2):
        if 0 <= next < MAX and not visited[next]:
            visited[next] = True
            parent[next] = current
            dist[next] = dist[current] + 1
            queue.append(next)

path = []
current = K
while current != -1:
    path.append(current)
    current = parent[current]

print(dist[K])
print(*reversed(path))

    