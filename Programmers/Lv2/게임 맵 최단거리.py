from collections import deque
def solution(maps):
    # n x m 크기의 맵
    n = len(maps)
    m = len(maps[0])
    # 상하좌우 이동
    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(1, 1)])
    visited = [[-1] * (m+1) for _ in range(n+1)]
    visited[1][1] = 1
    while queue: 
        (x, y) = queue.popleft()
        if x == n and y == m: break
        for dx, dy in dt:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= m and visited[nx][ny] == -1 and maps[nx-1][ny-1] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited[n][m]