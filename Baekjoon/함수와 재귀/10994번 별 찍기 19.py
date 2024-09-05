import sys
read = sys.stdin.readline

N = int(read())

s = 4 * N - 3 # 제일 큰 변의 길이
stars = [[' ' for _ in range(s)] for _ in range(s)]

# (start, start): 가장 윗줄 왼쪽 별의 위치 
def draw(N, start, stars):
    # 종료 조건
    if (N == 0): return
    # 그림 그리기
    n = 4 * N - 3 # 한 변의 길이
    for i in range(0, n):
        stars[start + i][start] = "*"
        stars[start + i][start + n - 1] = "*"
        stars[start][start + i] = "*"
        stars[start + n - 1][start + i] = "*"
    return draw(N-1, start+2, stars)

draw(N, 0, stars)

# 출력
for i in range(s):
    for j in range(s):
        print(stars[i][j], end="")
    print("")