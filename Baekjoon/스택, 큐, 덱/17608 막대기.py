import sys
read = sys.stdin.readline

N = int(read())
stack = []

for _ in range(N):
    bar = int(read())
    # 현재 막대기의 가장 오른쪽 요소보다 내가 작을 때까지 pop
    while stack and stack[-1] <= bar:
        stack.pop()
    stack.append(bar)

print(len(stack))