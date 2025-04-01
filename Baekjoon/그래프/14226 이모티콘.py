import sys
from collections import deque
read = sys.stdin.readline

S = int(read())

MAX = 1001
visited = [[False] * MAX for _ in range(MAX)]
visited[1][0] = True
queue = deque([(1, 0, 0)]) # (display, clipboard, count)

while queue:
    display, clipboard, count = queue.popleft()
    if display == S: 
        print(count)
        break
    # 연산 1
    if not visited[display][display]:
        queue.append((display, display, count+1))
        visited[display][display] = True
    # 연산 2
    if clipboard != 0 and display + clipboard < MAX and not visited[display+clipboard][clipboard]:
        queue.append((display + clipboard, clipboard, count+1))
        visited[display+clipboard][clipboard] = True
    # 연산 3
    if display > 0 and not visited[display-1][clipboard]:
        queue.append((display-1, clipboard, count+1))
        visited[display-1][clipboard] = True
