import sys
from itertools import combinations
read = sys.stdin.readline

N, M = map(int, read().split())
city = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))
            
def get_city_chicken_distance(active_chickens):
    total = 0
    for hx, hy in homes:
        min_dist = float('inf')
        for cx, cy in active_chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        total += min_dist
    return total

def use_combination():
    result = float('inf')
    for comb in combinations(chickens, M):
        dist = get_city_chicken_distance(comb)
        result = min(result, dist)
    print(result)

min_total = float('inf')
def dfs(start, selected):
    global min_total
    if len(selected) == M:
        total = 0
        for hx, hy in homes:
            min_dist = float('inf')
            for cx, cy in selected:
                dist = abs(hx - cx) + abs(hy - cy)
                min_dist = min(min_dist, dist)
            total += min_dist
        min_total = min(min_total, total)
        return
    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        dfs(i + 1, selected)
        selected.pop()
        
def use_dfs():
    dfs(0, [])
    print(min_total)
    
use_dfs()