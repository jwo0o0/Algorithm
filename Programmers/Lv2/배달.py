from collections import defaultdict

def solution(N, road, K):
    # 마을 N개, 최대 배달 시간 K
    # 시작 노드 1
    graph = defaultdict(list)
    for [a, b, c] in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 방문 여부와 걸리는 시간을 저장하는 배열
    visited = [False] * (N + 1)
    visited[1] = True
    distance = [0] * (N + 1)
    # bfs 탐색
    queue = [1]
    while queue:
        current = queue.pop()
        for (adjacent, k) in graph[current]:
            new_k = distance[current] + k
            # 방문하지 않았거나 배달 시간을 적게 갱신하는 경우
            if not visited[adjacent] or new_k < distance[adjacent]:
                distance[adjacent] = new_k
                visited[adjacent] = True
                queue.append(adjacent) 
    answer = 0
    for k in distance[1:]:
        if k <= K: answer += 1

    return answer