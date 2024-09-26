import sys
read = sys.stdin.readline

X = read().strip()

count = 0
# X가 한자리 수가 될때까지
while (len(X) != 1):
    count += 1
    sum = 0
    # X의 모든 자리수를 더하고 다시 문자열로 변환
    for x in X:
        sum += int(x)
    X = str(sum)

print(count)
print('YES' if X in ['3', '6', '9'] else 'NO')