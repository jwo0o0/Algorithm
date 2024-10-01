import sys
from collections import deque
read = sys.stdin.readline

queue = deque()
max_num = 0
min_student = 100000

N = int(read())
for _ in range(N):
    info = list(map(int, read().split()))
    # 유형 1
    # 큐에 학생 번호 추가
    if info[0] == 1:
        queue.append(info[1])
        # 최대 대기줄 크기를 넘은 경우 
        if (len(queue) > max_num):
            max_num += 1
            min_student = info[1]
        # 최대 대기줄 크기가 같은 경우 -> 큐의 top 비교
        elif (len(queue) == max_num):
            if (min_student > info[1]):
                min_student = info[1]
    # 유형 2
    elif info[0] == 2:
        queue.popleft()

print(max_num, min_student)