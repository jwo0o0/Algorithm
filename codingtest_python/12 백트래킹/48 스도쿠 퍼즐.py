def solution(board):
    # 유망 함수
    def promising(row, col, num):
        if board[row].count(num): 
            return False
        elif any(rows[col] == num for rows in board):
            return False
        else:
            n_row, n_col = (row // 3) * 3, (col // 3) * 3
            for r in range(n_row, n_row + 3):
                for c in range(n_col, n_col + 3):
                    if board[r][c] == num:
                        return False
        return True
    
    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def find_solution():
        empty = find_empty()
        if not empty: return True
        row, col = empty
        for num in range(1, 10):
            if promising(row, col, num):
                board[row][col] = num
                if find_solution(): # 다음 빈칸을 재귀 탐색
                    return True
                board[row][col] = 0 # 가능한 숫자가 없으면 원래의 0으로 되돌림
        return False
    
    find_solution()
    return board

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
result = solution(board)
for r in result: print(r)