import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())

# 1부터 N까지 저장되어 있는 큐
arr = deque()
for i in range(N):
    arr.append(i + 1)

answer = []
for _ in range(N):
    # K-1번만큼 큐에서 pop하고 다시 push
    for _ in range(K-1):
        arr.append(arr.popleft())
    # 큐에서 pop해서 순열에 추가
    answer.append(arr.popleft())

print(f"<{', '.join(map(str, answer))}>")
