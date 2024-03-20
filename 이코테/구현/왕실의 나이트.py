# 왕실의 나이트
n = input()

x_dict = {
    'a':1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6, 
    'g': 7,
    'h': 8
}
x = x_dict[n[0]]
y = int(n[1])

dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, -2, -2, 2, 2]

count = 0

for i in range (0, 8):
    hx = x + dx[i]
    hy = y + dy[i]
    if (hx < 1 or hx > 8 or hy < 1 or hy > 8):
        continue
    else: 
        count += 1

print(count)