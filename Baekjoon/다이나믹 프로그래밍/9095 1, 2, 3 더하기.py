import sys
read = sys.stdin.readline

T = int(read())
answer = [1, 2, 4]
for i in range(3, 11):
    answer.append(answer[i-3] + answer[i-2] + answer[i-1])

for _ in range(T):
    n = int(read())
    print(answer[n-1])