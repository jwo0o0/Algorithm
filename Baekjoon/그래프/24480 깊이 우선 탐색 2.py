import sys
read = sys.stdin.readline

# N개의 정점, M개의 간선, 시작 정점 R
N, M, R = map(int, read().split())

# 인접 행렬 사용시 메모리 초과 -> 인접 리스트로 그래프 저장
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

order = 1 # 방문 순서
result = [0] * (N + 1) # 방문 순서를 저장

visited = [False] * (N + 1)
stack = [R]
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        result[node] = order
        order += 1
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                stack.append(neighbor)

for n in result[1:]: print(n)