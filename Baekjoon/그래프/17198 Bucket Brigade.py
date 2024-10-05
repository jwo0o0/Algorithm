import sys
from collections import deque
read = sys.stdin.readline

farm = []
for _ in range(10):
    farm.append(list(read().strip()))

# B와 L의 좌표 저장
b_x, b_y, l_x, l_y = 0, 0, 0, 0
for i in range(10):
    for j in range(10):
        if farm[i][j] == 'B':
            b_x, b_y = i, j
        elif farm[i][j] == 'L':
            l_x, l_y = i, j

visited = [[0] * 10 for _ in range(10)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# bfs로 B에서 L까지의 경로 탐색
queue = deque([(b_x, b_y)])
visited[b_x][b_y] = 0
while queue:
    x, y = queue.popleft()
    # L이 나오면 탐색 중지
    if farm[x][y] == 'L':
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내에 있고 R이 아닌 경우 이어서 탐색
        if nx in range(0, 10) and ny in range(0, 10) and not visited[nx][ny] and farm[nx][ny] != 'R':
            queue.append((nx, ny))
            # 지금까지 왔던 경로의 수 + 1
            visited[nx][ny] = visited[x][y] + 1

# L의 좌표까지 가는 수 - 1
print(visited[l_x][l_y] - 1)