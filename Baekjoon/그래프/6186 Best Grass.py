import sys
read = sys.stdin.readline 

R, C = map(int, read().split()) # 행, 열
grass = [list(read().strip()) for _ in range(R)]

count = 0 # 잔디 구역의 개수

# 상하좌우 이동시 좌표 변화
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def search(r, c):
    # 해당 구역을 방문 처리
    grass[r][c] = '.'
    # 상하좌우 탐색
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        # 인접한 잔디가 있으면 방문
        if x >= 0 and x < R and y >= 0 and y < C and grass[x][y] == '#':
            search(r+dx[i], c+dy[i])

for r in range(R):
    for c in range(C):
        # 잔디가 있다면 찾기를 시작
        if grass[r][c] == '#':
            search(r, c)
            count += 1
        
print(count)

# 시간 복잡도
# 조건: 1 <= R, C <= 100
# O(R*C)