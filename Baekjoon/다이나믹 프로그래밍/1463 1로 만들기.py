import sys
from collections import deque
read = sys.stdin.readline

N = int(read())

min_count = 0
queue = deque([(N, 0)])
visited = set([N])
while queue:
    current, count = queue.popleft()
    if current == 1:
        min_count = count
        break
    if current % 3 == 0 and (current / 3) not in visited:
        queue.append((int(current / 3), count + 1))
        visited.add(int(current / 3))
    if current % 2 == 0 and (current / 2) not in visited:
        queue.append((int(current / 2), count + 1))
        visited.add(int(current / 2))
    if current - 1 > 0 and (current - 1) not in visited:
        queue.append((current - 1, count + 1))
        visited.add(current - 1)
    
print(min_count)