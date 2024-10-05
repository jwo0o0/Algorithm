import sys
read = sys.stdin.readline 

N, M = map(int, read().split())
trees = list(map(int, read().split()))

start, end = 0, max(trees) # 이진 탐색의 최소, 최댓값
H = (start + end) // 2 # 절단기 높이의 최댓값

# 0 ~ 트리의 최대 높이에서 이진 탐색 시작
while start <= end:
    # 적어도 M미터의 나무를 가져갈 수 있는지 확인
    tree_cut = 0
    for t in trees:
        tree_cut += t - H if t - H > 0 else 0
    # M미터를 가져갈 수 있으면 그 위의 범위를 탐색
    if tree_cut >= M:
        start = H + 1
    # 가져갈 수 없으면 아래의 범위를 탐색
    else:
        end = H - 1
    H = (start + end) // 2

print(H)