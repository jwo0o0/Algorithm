import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
read = sys.stdin.readline

N, M = map(int, read().split()) # N개의 정점과 M개의 간선

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    
S = int(read()) # 곰곰이가 존재하는 정점의 개수
goms = list(map(int, read().split())) # 곰곰이가 존재하는 정점의 번호

result = 'Yes' # 결과
visited = [False] * (N+1) # 방문 여부를 저장

# 1) DFS 재귀로 구현
# def dfs_recur(node, find):
#     global result
#     visited[node] = True # 현재 노드 방문 처리
#     # 팬클럼 곰곰이를 만났다면 탐색 종료
#     if node in goms:
#         return
#     # 더 이상 탐색할 노드가 없는 경우 곰곰이를 만나지 않았으면 결과를 바꿈
#     if not graph[node] and not find:
#         result = 'yes'
#     # 인접한 방문하지 않은 노드를 탐색
#     for next_node in graph[node]:
#         if not visited[next_node]:
#             dfs_recur(next_node, find)
            
# dfs_recur(1, False)
# print(result)

# 2) DFS 스택으로 구현
stack = []
def dfs_stack(start):
    stack.append(start)
    visited[start] = True
    while stack:
        node = stack.pop()
        visited[node] = True
        # 곰곰이를 만났으면 이어서 탐색하지 않음
        if node in goms: 
            continue
        # 탐색할 노드가 없는 경우
        # -> 곰곰이를 만나지 않았으면 'yes' 리턴
        if not graph[node]:
            return 'yes'
        for next_node in graph[node]:
            if not visited[next_node]:
                stack.append(next_node)
    # 곰곰이를 만나지 않고 끝까지 탐색한 경우가 없다면 'Yes' 리턴
    return 'Yes'
                
print(dfs_stack(1))
