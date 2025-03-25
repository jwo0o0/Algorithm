import heapq

# graph: 딕셔너리, start: 시작 노드
# 반환 값: 시작 노드부터 각 노드까지 최소 비용과 최단 경로를 포함한 리스트
# 그래프의 노드 개수는 최대 10,000개
# 각 노드는 0 이상의 정수
# 가중치는 0 이상, 10,000 이하

def solution(graph, start):
    # 모든 노드의 거리 값을 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0     # 시작 노드의 거리 값은 0으로 초기화
    queue = []
    heapq.heappush(queue, [distances[start], start]) # 시작 노드를 큐에 삽입
    paths = {start: [start]} # 시작 노드의 경로를 초기화
    
    while queue: 
        # 현재 가장 거리 값이 작은 노드를 가져옴
        current_distance, current_node = heapq.heappop(queue)
        # 현재 노드의 거리 값 > 큐에서 거리온 거리 값 => 해당 노드는 이미 처리한 것이므로 무시
        if distances[current_node] < current_distance:
            continue
        # 현재 노드와 인접한 노드들의 거리 값을 계산해 업데이트
        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            # 현재 계산한 거리 값 < 기존 거리 값이면 최소 비용 및 최단 경로 업데이트
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                paths[adjacent_node] = paths[current_node] + [adjacent_node]
                # 최소 경로가 갱신된 노드를 비용과 함께 큐에 푸시
                heapq.heappush(queue, [distance, adjacent_node])
    # paths 딕셔너리를 노드 번호에 따라 오름차순 정렬
    sorted_paths = {node: paths[node] for node in sorted(paths)}
       
    return [distances, sorted_paths]

graph = {
    'A': {'B': 9, 'C': 3}, 
    'B': {'A': 5},
    'C': {'B': 1}
}
start = 'A'

print(solution(graph, start))