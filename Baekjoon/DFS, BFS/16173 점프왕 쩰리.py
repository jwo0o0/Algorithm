import sys
read = sys.stdin.readline 

N = int(read())
game = [list(map(int, read().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # 방문 체크 리스트

def jump(r, c):
    # 게임 종료 조건
    # 1. 구역 외부로 나가거나 이미 방문한 경우
    if r >= N or c >= N or visited[r][c]:
        return False
    # 게임을 승리한 경우
    if game[r][c] == -1:
        return True
    # 현재 위치 방문 표시
    visited[r][c] = True
    # 오른쪽 / 아래 방향으로 게임 진행
    return jump(r, c + game[r][c]) or jump(r + game[r][c], c)

if jump(0, 0): print('HaruHaru')
else: print('Hing')

# 시간 복잡도
# DFS 탐색이므로 O(N^2)