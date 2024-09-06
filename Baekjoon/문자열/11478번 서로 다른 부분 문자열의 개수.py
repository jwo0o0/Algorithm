import sys
read = sys.stdin.readline

# 1부터 문자열 S의 길이까지 반복하며
# S의 처음부터 부분 문자열을 구하고
# 중복이 없는 set에 저장
S = read().strip()
set = set()
for n in range(1, len(S) + 1): # 부분 문자열의 길이
    for s in range(0, len(S) - n + 1): # 부분 문자열의 시작 위치
        set.add(S[s:s+n])

print(len(set))
