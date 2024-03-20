# 상하좌우
n = int(input())
data = list(map(str, input().split()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 1, 1

for i in data:
    tmp_x, tmp_y = x, y
    if (i == 'R'):
        tmp_x += dx[0]
        tmp_y += dy[0]
    elif (i == 'U'):
        tmp_x += dx[1]
        tmp_y += dy[1]
    elif (i == 'L'):
        tmp_x += dx[2]
        tmp_y += dy[2]
    elif (i == 'D'):
        tmp_x += dx[3]
        tmp_y += dy[3]
    if (0 < tmp_x <= n and 0 < tmp_y <= n):
        x, y = tmp_x, tmp_y

print(x, y)