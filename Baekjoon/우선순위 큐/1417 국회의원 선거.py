import sys
import heapq
read = sys.stdin.readline

N = int(read()) # 후보의 수
D = int(read()) # 다솜이를 찍으려는 사람의 수

# 기호 2번부터 N명의 후보를 찍으려고 하는 사람의 수
# 투표자 수가 많은 후보자부터 매수해야하므로 우선순위 큐 사용
votes = [] 
for _ in range(N - 1):
    heapq.heappush(votes, -int(read()))

count = 0 # 매수하는 사람의 수
while (votes): # 후보자가 한명인 경우 pass
    # 종료 조건: 가장 득표수가 많은 사람 < 다솜이의 득표수 + 매수한 득표수가 될때까지
    max_vote = -heapq.heappop(votes)
    if (D + count > max_vote): break
    # 조건을 만족하지 못하면 한 명 더 매수, 다시 최대 힙에 push
    count += 1
    heapq.heappush(votes, -int(max_vote - 1))
    
print(count)