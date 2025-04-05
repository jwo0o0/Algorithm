import sys
from collections import deque
read = sys.stdin.readline

M, N = map(int, read().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0

queue = deque([(0, 0)])
dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in dt:
        nx, ny = x + dx, y + dy
        if nx in range(N) and ny in range(M):
            # 아직 방문하지 않았거나 더 나은 경로인 경우
            if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + miro[nx][ny]:
                dist[nx][ny] = dist[x][y] + miro[nx][ny]
                if miro[nx][ny] == 0:
                    queue.appendleft((nx, ny))
                else:
                    queue.append((nx, ny))

print(dist[N - 1][M - 1])