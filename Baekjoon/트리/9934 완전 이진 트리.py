import sys
read = sys.stdin.readline

K = int(read())
buildings = [0]
buildings += list(map(int, read().split()))

# 각 레벨의 노드를 저장할 딕셔너리
tree = {}
for k in range(1, K+1):
    tree[k] = []

def get_child_nodes(index, degree):
    global K
    # 해당 레벨의 노드 리스트에 추가
    tree[degree].append(buildings[index])
    # 가장 높은 차수가 되면 return
    if degree == K: return
    # 왼쪽과 오른쪽 자식 노드로 이동 
    # 레벨에 따라 index의 위치가 value만큼 이동
    value = int(2 ** (K - degree - 1))
    get_child_nodes(index - value, degree + 1)
    get_child_nodes(index + value, degree + 1)
    
# 루트 노드의 인덱스
root_node_index = 2 ** (K - 1)
get_child_nodes(root_node_index, 1)

# 각 차수의 노드 출력
for nodes in tree.values():
    print(' '.join(map(str, nodes)))
    
# 시간 복잡도
# 입력: 1 <= K <= 10
# O(2^K)