import sys
from collections import deque
read = sys.stdin.readline

# 총 F층, 현재 S층에서 G층으로 이동
# +U, -D만큼 이동 가능
F, S, G, U, D = map(int, read().split())

visited = [0] * (F + 1) # 0이면 미방문, 1 이상이면 방문한 상태
visited[S] = 1 # 시작 위치를 방문했다고 표시하지 않으면 재방문할 수 있음
queue = deque([S])
while queue:
    current = queue.popleft()
    if current == G: break
    for move in [U, -D]:
        if 1 <= current + move <= F and visited[current + move] == 0:
            visited[current + move] = visited[current] + 1
            queue.append(current + move)

print('use the stairs' if visited[G] == 0 else visited[G] - 1)

# 시간복잡도: O(F)
# 최악의 겨우 모든 층을 한번씩 방문