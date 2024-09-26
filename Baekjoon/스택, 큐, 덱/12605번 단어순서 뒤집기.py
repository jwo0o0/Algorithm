import sys
read = sys.stdin.readline

N = int(input())

cases = []
for i in range(N):
    # 케이스를 스페이스로 분리하고 반대로 바꾼 후 저장
    case = list(read().strip().split())
    case.reverse()
    cases.append(case)

# 저장된 케이스를 순회하며 출력
for idx, case in enumerate(cases):
    print(f"Case #{idx+1}: {' '.join(case)}")
    