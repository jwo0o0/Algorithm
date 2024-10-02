import sys
read = sys.stdin.readline 

N = int(read())

skylines = []
min_count = 0
for _ in range(N):
    x, y = map(int, read().split())
    # 스택이 비어있다면 push
    if not skylines:
        skylines.append(y)
        continue
    # 이전 건물의 높이보다 낮으면 pop하고 개수 세기
    while skylines and y < skylines[-1]:
        skylines.pop()
        min_count += 1
    # 높이가 같으면 pass
    if skylines and y > skylines[-1]:
        continue
    # 스택에 추가
    skylines.append(y)

# 남아있는 건물들의 높이가 0이 아니면 개수 세기
while skylines:
    if skylines[-1] > 0: min_count += 1
    skylines.pop()
       
print(min_count)
