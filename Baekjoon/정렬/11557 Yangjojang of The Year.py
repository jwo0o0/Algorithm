import sys
read = sys.stdin.readline

T = int(read())
result = []
for _ in range(T):
    N = int(read())
    max, max_s = 0, ''
    for _ in range(N):
        S, L = read().split()
        # 최댓값과 학교 이름을 비교해 갱신
        if int(L) > max:
            max_s = S
            max = int(L)
    result.append(max_s)
    
for r in result: 
    print(r)