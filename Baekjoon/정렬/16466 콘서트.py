import sys
read = sys.stdin.readline

N = int(read())
sold = list(map(int, read().split()))
# 1번 티켓부터 확인하며 팔리지 않았으면 출력
min_ticket = 1000001
# 티켓이 팔렸는지 여부를 저장
tickets = [False] * 1000001
# 팔린 티켓의 경우 tickets의 값을 True로
for s in sold:
    tickets[s] = True
# 1번부터 값이 확인하며 tickets의 값이 True인지 확인
for i in range(1, 1000001):
    if not tickets[i]: 
        min_ticket = i
        break
print(min_ticket)