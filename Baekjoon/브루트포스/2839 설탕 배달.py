import sys
read = sys.stdin.readline

N = int(read())

result = -1

# 5킬로그램 봉지 a개, 3킬로그램 봉지 3개
# a개의 최대 개수 -> 0개인 경우까지 계산
for a in range(N // 5, -1, -1):
    left = N - 5 * a
    if (left % 3 == 0):
        result = a + left // 3
        break
    
print(result)
    


