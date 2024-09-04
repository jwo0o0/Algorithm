def solution(arr1, arr2):
    answer = []
    # solution 행렬의 행수
    N = len(arr1)
    M = len(arr2[0])
    K = len(arr1[0])
    # 행렬 곱셈
    for i in range(N):
        tmp = []
        for j in range(M):
            # i행 j열의 원소 구하기
            sum = 0
            for k in range(K):
                sum += arr1[i][k] * arr2[k][j]
            tmp.append(sum)
        answer.append(tmp)
    
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

print(solution(arr1, arr2))