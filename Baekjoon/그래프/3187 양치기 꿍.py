import sys
from collections import deque
read = sys.stdin.readline

R, C = map(int, read().split()) # 세로, 가로
map = [list(read().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
k, v = 0, 0 # 양, 늑대

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def bfs(x, y):
    global k, v
    sheep, wolf = 0, 0 # 구역 내의 양과 늑대의 수
    queue = deque([[x, y]])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        if map[x][y] == 'v': wolf += 1
        elif map[x][y] == 'k': sheep += 1
        # 상하좌우로 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고 울타리가 아니며 방문하지 않은 경우
            if nx in range(R) and ny in range(C) and map[nx][ny] != '#' and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                
    # 양과 늑대의 수에 따라 총합에 더함            
    if sheep > wolf: k += sheep
    else: v += wolf

# 울타리가 아니고 방문하지 않은 경우 bfs 탐색을 시작
for x in range(R):
    for y in range(C):
        if map[x][y] != '#' and not visited[x][y]:
            bfs(x, y)

print(k, v)

# 시간 복잡도
# 입력: 3 <= R, C <= 250
# O(R*C)