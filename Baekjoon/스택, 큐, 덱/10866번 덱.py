import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
D = deque()
for _ in range(N):
    inputs = read().split()
    if (inputs[0] == 'push_front'):
        D.appendleft(int(inputs[1]))
    elif (inputs[0] == 'push_back'):
        D.append(int(inputs[1]))
    elif (inputs[0] == 'pop_front'):
        print(D.popleft() if len(D) > 0 else -1)
    elif (inputs[0] == 'pop_back'):
        print(D.pop() if len(D) > 0 else -1)
    elif (inputs[0] == 'size'):
        print(len(D))
    elif (inputs[0] == 'empty'):
        print(1 if len(D) == 0 else 0)
    elif (inputs[0] == 'front'):
        print(D[0] if len(D) > 0 else -1)
    elif (inputs[0] == 'back'):
        print(D[-1] if len(D) > 0 else -1)