import sys, heapq
read = sys.stdin.readline 

N, K = map(int, read().split())
quests = list(map(int, read().split())) # N개의 퀘스트의 경험치
stones = [False] * N # N개의 아케인 스톤의 활성화 여부

activate = 0 # 활성화 되어 있는 스톤의 개수
exp = 0 # 경험치의 합
heapq.heapify(quests) # 퀘스트의 목록을 최소 힙으로 변환

# 모든 퀘스트를 수행할 때까지
# 경험치가 작은 퀘스트부터 수행
while quests:
    # 스톤이 K개만큼 활성화 되지 않은 경우
    # -> 활성화된 스톤 * 경험치를 획득
    # -> 스톤 1개 활성화
    if (activate < K):
        exp += activate * heapq.heappop(quests)
        activate += 1
    # 스톤이 K개 활성화 된 경우
    # -> K * 경험치를 획득
    elif (activate >= K):
        exp += K * heapq.heappop(quests)

print(exp)