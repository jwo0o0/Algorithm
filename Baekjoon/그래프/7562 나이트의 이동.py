import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
result = []

# 나이트가 이동 가능한 경우
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

# bfs 탐색 (start_x, start_y)에서 시작해 (end_x, end_y)에 도달할 때까지
def bfs(graph, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        # 목표에 도달하면 return
        if x == end_x and y == end_y:
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 체스판 안에 있고 아직 방문하지 않은 칸이라면 방문 순서를 갱신
            if nx in range(0, len(graph)) and ny in range(0, len(graph)) and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


for _ in range(T):
    L = int(read())
    start_x, start_y = map(int, read().split())
    end_x, end_y = map(int, read().split())
    # 체스판
    graph = [[0] * L for _ in range(L)]
    bfs(graph, start_x, start_y, end_x, end_y)
    result.append(graph[end_x][end_y])

for r in result: print(r)