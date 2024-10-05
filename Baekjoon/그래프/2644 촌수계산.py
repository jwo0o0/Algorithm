import sys
from collections import defaultdict
read = sys.stdin.readline 

N = int(read()) # 전체 사람의 수
A, B = map(int, read().split()) # 촌수를 구해야 할 두 사람
M = int(read())

graph = defaultdict(list) # 그래프를 인접리스트로 저장

for _ in range(M):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)
    
distance = [False] * (N+1) # 방문했는지 여부
result = 0

def dfs(node, count):
    global result
    # 찾고자 하는 사람이면 탐색을 중단
    if node == B: 
        result = count
        return
    distance[node] = True
    # 인접한 사람을 탐색하지 않았으면 촌수를 늘리고 계속 탐색
    for next_node in graph[node]:
        if not distance[next_node]:
            dfs(next_node, count + 1)
            
dfs(A, 0)
print(result if result > 0 else -1)