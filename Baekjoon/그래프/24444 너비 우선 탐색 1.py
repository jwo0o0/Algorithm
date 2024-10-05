import sys
from collections import defaultdict, deque
read = sys.stdin.readline

N, M, R = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1) # 방문 여부
visited_nth = [0] * (N+1) # 노드의 방문 순서

def bfs(start):
    queue = deque([start])
    visited[start] = True
    visited_nth[start] = 1
    count = 1
    while queue:
        # 새로운 노드를 방문하고 순서를 +1
        node = queue.popleft()
        visited_nth[node] = count
        count += 1
        # 다음으로 방문할 노드의 목록
        next_visit = []
        for next_node in graph[node]:
            if not visited[next_node]:
                next_visit.append(next_node)
                visited[next_node] = True
        # 노드를 오름차순으로 방문하므로 sort해서 큐에 저장
        queue.extend(sorted(next_visit))
            
bfs(R)
for n in visited_nth[1:]: print(n)