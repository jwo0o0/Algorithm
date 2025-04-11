import sys
from collections import defaultdict
read = sys.stdin.readline

N, M = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

found = False
visited = [False] * N

def dfs(current, depth):
    global found
    if found: return
    if depth == 5:
        found = True
        return
    visited[current] = True
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
    visited[current] = False
    
for i in range(N):
    dfs(i, 1)
    if found: break

print(1 if found else 0)
    
