import sys
from collections import defaultdict
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    # 옷의 종류와 개수를 저장할 딕셔너리
    wears = defaultdict(int)
    N = int(read())
    for _ in range(N):
        name, type = read().strip().split()
        wears[type] += 1
    
    # 경우를 곱해줘야하므로 1로 초기화    
    count = 1
    # 해당 옷을 입지 않는 경우도 있으므로 +1
    for w in wears: 
        count *= (wears[w] + 1)
    # 알몸인 경우를 제외해야 하므로 -1
    print(count - 1)