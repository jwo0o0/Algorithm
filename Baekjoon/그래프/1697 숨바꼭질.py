import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())
visited = [False] * 100001

# 수빈이가 위동할 수 있는 위치
def move(n, i):
    if i == 0: return n + 1
    elif i == 1: return n - 1
    elif i == 2: return n * 2

def bfs(start, K):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        n, count = queue.popleft()
        # 동생을 찾으면 그만 탐색
        if n == K:
            return count
        for i in range(3):
            moved_n = move(n, i)
            if moved_n in range(0, 100001) and not visited[moved_n]:
                queue.append((moved_n, count + 1))
                visited[moved_n] = True

print(bfs(N, K))
