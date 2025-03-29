def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    max_count = 0
    
    def backtrack(fatigue, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        # 최대로 탐색해도 max_count를 못 넘으면 중단
        if count + (n - sum(visited)) <= max_count:
            return
        
        for i in range(n):
            min_req, cost = dungeons[i]
            if not visited[i] and fatigue >= min_req:
                visited[i] = True
                backtrack(fatigue - cost, count + 1)
                visited[i] = False # 백트래킹
    
    backtrack(k, 0)
    return max_count