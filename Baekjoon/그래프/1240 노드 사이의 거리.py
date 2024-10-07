import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N, M = map(int, read().split())
# 노드 x-y 사이의 거리가 r인 그래프를 인접 리스트로 저장
graph = defaultdict(list)
for _ in range(N-1):
    x, y, r = map(int, read().split())
    graph[x].append((y, r))
    graph[y].append((x, r))
    
def bfs(start, end,  graph):
    visited = [False] * (N+1)
    queue = deque([(start, 0)]) # (현재 노드, 현재까지의 거리)
    visited[start] = True
    while queue:
        node, dist = queue.popleft()
        # 찾고자 하는 노드에 도달하면 현재까지의 거리를 반환
        if node == end:
            return dist
        # 인접한 노드를 방문
        for next_node, d in graph[node]:
            if not visited[next_node]:
                queue.append((next_node, dist + d))
                visited[next_node] = True
                
for _ in range(M):
    x, y = map(int, read().split())
    print(bfs(x, y, graph))
    
# 시간 복잡도
# 각 그래프 탐색시 O(N + (N-1)) = O(N)
# M번 반복하므로 O(N * M)