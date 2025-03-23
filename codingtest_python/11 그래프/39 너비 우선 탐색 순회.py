from collections import defaultdict, deque

def solution(start, graph):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    print(adj_list)
    # bfs 탐색
    visited = set()
    visited.add(start)
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return result

graph = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
graph2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
print(solution(1, graph2))
