import sys
from collections import deque
read = sys.stdin.readline

M, N, H = map(int, read().split()) # 가로, 세로, 높이
tomatoes = []
for h in range(H):
    tomatoes.append([])
    for _ in range(N):
        tomatoes[h].append(list(map(int, read().split())))

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

def bfs(queue):
    count = -1 # 모든 토마토를 탐색할 때까지 걸리는 일수
    tmp_queue = deque()
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx in range(0, M) and ny in range(0, N) and nz in range(0, H):
                # 내가 익은 토마토이고 인접한 곳이 아직 익지 않은 토마토라면
                if tomatoes[z][y][x] == 1 and tomatoes[nz][ny][nx] == 0:
                    tmp_queue.append((nx, ny, nz)) # 다음날 탐색해야하므로 임시 큐에 push
                    tomatoes[nz][ny][nx] = 1 # 토마토를 익게함
        # 오늘 익은 토마토의 인접 토마토를 모두 탐색했다면
        if not queue: 
            queue.extend(tmp_queue) # 큐에 임시 큐를 넣고
            tmp_queue.clear() # 임시 큐를 비움
            count += 1
    return count

queue = deque() # bfs 탐색에 사용할 큐
# 처음에 1인 토마토를 찾아 큐에 push하고 bfs 탐색을 시작
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append((m, n, h))
                
result = bfs(queue)
                
find_zero = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                find_zero = True
                
print(-1 if find_zero else result)

