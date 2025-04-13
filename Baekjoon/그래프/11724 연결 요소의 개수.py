import sys
from collections import defaultdict, deque
read = sys.stdin.readline

graph = defaultdict(list)
N, M = map(int, read().split())
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return 1

for i in range(1, N+1):
    if not visited[i]: 
        answer += bfs(i)

print(answer)