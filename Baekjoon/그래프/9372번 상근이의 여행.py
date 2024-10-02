import sys
read = sys.stdin.readline 


T = int(read())

# 풀이 1)
# '비행기 종류'(=간선)의 최소 개수를 구하고,
# 다른 국가를 거쳐 이동해도 되므로 항상 N-1
for _ in range(T):
    N, M = map(int, read().split())
    for _ in range(M):
        a, b = map(int, read().split())
    print(N-1)
    
# 풀이 2)
# DFS로 탐색
# def search(graph, visited, country, count):
#     # 현재 국가를 방문 처리
#     visited[country] = True
#     # 인접한 국가로 방문
#     for next_country in graph[country]:
#         # 인접한 국가가 아직 방문하지 않은 곳이면
#         if not visited[next_country]:
#             count = search(graph, visited, next_country, count+1)
#     return count

# for _ in range(T):
#     N, M = map(int, read().split())
#     graph = [[] for _ in range(N+1)] # 그래프 정보
#     visited = [False] * (N+1) # 각 국가의 방문 여부
#     for _ in range(M):
#         a, b = map(int, read().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     # 국가 1부터 탐색
#     print(search(graph, visited, 1, 0))    
