import sys
read = sys.stdin.readline

T = int(read())

# 인접한 배추로 이동할 좌표
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 배추밭을 탐색
# 배추가 심어져 있는 영역을 탐색하고 모두 0으로
def dfs(M, N, x, y, graph):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        graph[y][x] = 0
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if nx in range(0, M) and ny in range(0, N) and graph[ny][nx] == 1:
                stack.append((nx, ny))
    
for _ in range(T):
    M, N, K = map(int, read().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, read().split())
        graph[y][x] = 1
    count = 0
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1:
                dfs(M, N, m, n, graph)
                count += 1
    print(count)