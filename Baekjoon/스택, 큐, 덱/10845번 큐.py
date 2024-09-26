import sys
from collections import deque
read = sys.stdin.readline

N = int(input())

# 큐의 pop 구현을 위해 deque 자료구조 사용
queue = deque()
for _ in range(N):
    cmd = read().split()
    if (cmd[0] == 'push'):
        queue.append(cmd[1])
    elif (cmd[0] == 'pop'):
        print(queue.popleft() if queue else -1)
    elif (cmd[0] == 'size'):
        print(len(queue))
    elif (cmd[0] == 'empty'):
        print(0 if queue else 1)
    elif (cmd[0] == 'front'):
        print(queue[0] if queue else -1)
    elif (cmd[0] == 'back'):
        print(queue[-1] if queue else -1)
    