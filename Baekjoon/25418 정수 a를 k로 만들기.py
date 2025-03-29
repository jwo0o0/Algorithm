import sys
from collections import deque
read = sys.stdin.readline

A, K = map(int, read().split())
queue = deque([(A, 0)])
visited = set([A])

result = 0
while queue:
    current, count = queue.popleft()
    if current == K: 
        result = count
        break
    if current + 1 <= K and (current + 1) not in visited: 
        visited.add(current + 1)
        queue.append((current + 1, count + 1))
    if current * 2 <= K and (current * 2) not in visited:
        visited.add(current * 2)
        queue.append((current * 2, count + 1))

print(result)