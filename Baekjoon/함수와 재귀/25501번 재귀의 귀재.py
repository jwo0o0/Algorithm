import sys
read = sys.stdin.readline

# 매개변수: 문자열, 시작 위치, 끝 위치, 호출 횟수
def recursion(s, l, r, cnt):
    if (l >= r): return 1, cnt+1
    elif (s[l] != s[r]): return 0, cnt+1
    else: return recursion(s, l+1, r-1, cnt+1)

# 호출 횟수 cnt를 0으로 시작
def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

T = int(read())
for _ in range(T):
    S = read().strip()
    isP, cnt = isPalindrome(S)
    print(isP, cnt)