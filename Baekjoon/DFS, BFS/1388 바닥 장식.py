import sys
read = sys.stdin.readline 

N, M = map(int, read().split())
floor = [list(read().strip()) for _ in range(N)]

count = 0 # 필요한 나무 판자의 개수

def search(type, n, m):
    # 이미 카운트된 나무 판자라면 x로 표시
    floor[n][m] = 'x'
    # '-' 모양일 때
    if type == '-':
        # 나의 오른쪽 판자가 방 안에 있고 같은 모양이라면 이어서 탐색
        if m + 1 < M and floor[n][m+1] == '-':
            search('-', n, m + 1)
    # '|' 모양일 때
    elif type == '|':
        if n + 1 < N and floor[n+1][m] == '|':
            search('|', n + 1, m)

# 방 바닥을 차례로 탐색하며 나무 판자의 개수 찾기        
for n in range(N):
    for m in range(M):
        if floor[n][m] == '-' or floor[n][m] == '|':
            search(floor[n][m], n, m)
            count += 1

print(count)

# 시간 복잡도
# DFS 탐색이므로 O(N*M)