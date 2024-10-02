import sys
read = sys.stdin.readline

T = int(read())
result = []

# 이진 트리에서 부모 노드의 리스트를 반환
# n의 부모 노드
    # n == 짝수 -> n / 2
    # n == 홀수 -> (n - 1) / 2
# 루트 노드인 1이 될 때까지 반복
def get_parent(num):
    parents = [num] # 자기 자신을 포함해야 함
    while num > 1:
        if num % 2 == 0:
            parents.append(int(num / 2))
            num /= 2
        else:
            parents.append(int((num - 1) / 2))
            num = (num - 1) / 2   
    # 공통 노드를 구하기 위해 reverse해서 오름차순으로 반환   
    parents.reverse()  
    return parents

for _ in range(T):
    A, B = map(int, read().split())
    # 오름차순으로 정렬된 각 정수의 부모 노드 리스트
    parents_a = get_parent(A)
    parents_b = get_parent(B)
    # 공통된 최대 부모 노드 구하기
    min_len = len(parents_a) if len(parents_a) < len(parents_b) else len(parents_b)
    max_parent_node = 1
    for i in range(min_len):
        if parents_a[i] == parents_b[i]:
            max_parent_node = parents_a[i]
    result.append(max_parent_node * 10)

# 결과 출력
for r in result:
    print(r)
    
# 시간 복잡도
# 입력: 1 <= A, B <= 1023
# O(log max(A, B))