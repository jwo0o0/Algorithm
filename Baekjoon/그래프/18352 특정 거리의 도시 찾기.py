import sys
from collections import defaultdict, deque
read = sys.stdin.readline

N, M, K, X = map(int, read().split())

# 방향 그래프를 인접 리스트로 표현
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, read().split())
    graph[A].append(B)

# 방문할 수 없어도 거리가 0으로 측정되기 때문에 방문 여부를 따로 저장해야 함
visited = [False] * (N+1)
distance = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        city = queue.popleft()
        for next_city in graph[city]:
            # 아직 방문하지 않은 경우
            # -> 해당 도시를 방문하고 최단 거리를 갱신
            if not visited[next_city]:
                queue.append(next_city)
                visited[next_city] = True
                distance[next_city] = distance[city] + 1
                
# 도시 X에서 시작해서 N개의 모든 도시까지의 경로를 탐색
bfs(X)

find = False
# 최단 거리가 K이고 방문한 경우 출력
for i in range(1, N+1):
    if distance[i] == K and visited[i]: 
        print(i)
        find = True
# 조건에 해당하는 도시가 없는 경우 -1 출력
if not find:
    print(-1)