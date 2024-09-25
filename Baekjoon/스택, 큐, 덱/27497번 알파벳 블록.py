import sys
from collections import deque
read = sys.stdin.readline

N = int(read())

# 앞뒤에 추가 연산을 하므로 덱 사용 (문자열 연산보다 속도 빠름)
blocks = deque()
# 가장 나중에 추가된 블록을 알아야하므로 스택 자료구조 사용
stack = [] 
for _ in range(N):
    inputs = read().split()
    # 1 c 혹은 2 c 입력
    if (inputs[0] == '1'):
        blocks.append(inputs[1])
        stack.append('back')
    elif (inputs[0] == '2'):
        blocks.appendleft(inputs[1])
        stack.append('front')
    # 3 입력
    else:
        # 빈 문자열에 제거하지 않는지 확인
        if (stack):
            last = stack.pop()
            if (last == 'front'): 
                blocks.popleft()
            else:
                blocks.pop()

print(0 if len(blocks) == 0 else "".join(blocks))