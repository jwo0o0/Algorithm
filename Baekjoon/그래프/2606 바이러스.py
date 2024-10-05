import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read()) # N개의 컴퓨터
M = int(read())

computers = defaultdict(list) # 네트워크 인접 리스트
infected = [False] * (N+1) # 감염되었는지(방문했는지) 여부

for _ in range(M):
    c1, c2 = map(int, read().split())
    computers[c1].append(c2)
    computers[c2].append(c1)

def dfs(com):
    infected[com] = True
    # 아직 감염되지 않고 연결된 컴퓨터로 이동
    for next_com in computers[com]:
        if not infected[next_com]:
            dfs(next_com)

dfs(1)
result = infected.count(True)
print(result - 1) # 1번 컴퓨터를 제외하고 출력
        