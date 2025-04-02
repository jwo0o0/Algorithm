import sys
read = sys.stdin.readline

N = int(read()) # 이동하려는 채널
B = int(read()) # 망가진 채널의 개수
broken = []
if B > 0: broken = list(map(int, read().split()))

buttons = [] # 가능한 숫자 버튼
for i in range(10):
    if i not in broken:
        buttons.append(i)

min_diff = float('inf')
result = 0
def find_close_num(current, i):
    global min_diff, result
    if i == 0: 
        num = int(current)
        if abs(N - num) < min_diff: 
            min_diff = abs(N - num)
            result = num
        return
    for b in buttons:
        find_close_num(current + str(b), i - 1)

plus_or_minus = abs(N - 100)

if not buttons:
    print(abs(N - 100))
    exit()

for length in range(len(str(N)) - 1, len(str(N)) + 2):
    if length <= 0: continue
    find_close_num('', length)

print(min(plus_or_minus, len(str(result)) + abs(N - result)))