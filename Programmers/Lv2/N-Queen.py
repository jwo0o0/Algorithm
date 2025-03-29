def solution(n):
    count = 0
    board = [[0] * n for _ in range(n)]
    cols = [False] * n # 열 사용 여부
    diag1 = [False] * (2 * n) 
    diag2 = [False] * (2 * n)
    
    def backtrack(row):
        nonlocal count
        if row == n: 
            count += 1
            return
        # row 행의 퀸 자리를 정함
        for col in range(n):
            if not cols[col] and not diag1[row - col + n] and not diag2[row + col]:
                cols[col] = True
                diag1[row - col + n] = True
                diag2[row + col] = True

                backtrack(row + 1)
                
                cols[col] = False
                diag1[row - col + n] = False
                diag2[row + col] = False
    
    backtrack(0)
    
    return count