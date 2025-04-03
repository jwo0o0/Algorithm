import sys
from collections import defaultdict, deque
read = sys.stdin.readline

def check(V, graph):
    visited = [0] * (V+1) # 0: 미방문, 1 or -1로 구분
    # 연결이 끊긴 그래프일 수도 있으므로 전체 노드에 대해 반복
    for start in range(1, V+1):
        if visited[start] != 0: # 이미 방문했으면
            continue
        queue = deque([start])
        visited[start] = 1
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == 0:
                    visited[neighbor] = -visited[current] # 반대로 색칠
                    queue.append(neighbor)
                # 같은 색이면 이분 그래프 아님
                elif visited[neighbor] == visited[current]:
                    return False
    return True

result = []
K = int(read())
for _ in range(K):
    V, E = map(int, read().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)
    print('YES' if check(V, graph) else 'NO')