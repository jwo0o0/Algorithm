import sys
from collections import defaultdict
read = sys.stdin.readline 

N, M, R = map(int, read().split())
# 인접리스트로 그래프 저장
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1) # 방문 여부
visited_nth = [0] * (N+1) # 노드의 방문 순서

def dfs(start):
    count = 0 # 방문 순서를 카운트
    stack = [start]
    while stack:
        node = stack.pop()
        # 아직 방문하지 않은 경우
        if not visited[node]:
            visited[node] = True  
            count += 1 
            visited_nth[node] = count
            # 현재 노드에서 다음으로 방문할 노드를 스택에 추가
            # 노드를 오름차순으로 방문하므로 내림차순으로 추가
            next_visit = sorted(graph[node], reverse=True)
            stack.extend(next_visit)
                
dfs(R)
for n in visited_nth[1:]:
    print(n)


