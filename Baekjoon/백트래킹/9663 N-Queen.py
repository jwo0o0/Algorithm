import sys
read = sys.stdin.readline

N = int(read())
board = [[0] * N for _ in range(N)]
cols = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)

count = 0
def check(row):
    global count
    if row == N: 
        count += 1
        return
    for col in range(N):
        # row행 col열에 놓을 수 있는 경우
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N]:
            board[col] = 1
            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + N] = True
            check(row + 1)
            board[col] = 0
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + N] = False

check(0)
print(count)
