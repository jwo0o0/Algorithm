import sys
read = sys.stdin.readline 

map = []
for _ in range(5):
    map.append(list(read().split()))
  
# 만들 수 있는 모든 여섯 자리 수  
# 중복을 제거하기 위해 set 사용
numbers = set()

# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def serach(x, y, number):
    # 숫자판의 범위를 벗어나면 종료
    if x < 0 or x > 4 or y < 0 or y > 4:
        return
    # 새로운 숫자를 더함
    number += map[x][y]
    # 숫자가 여섯 자리이면 set에 더하고 탐색을 종료
    if len(number) == 6: 
        numbers.add(number)
        return
    # 이어서 상하좌우 방향으로 탐색
    for i in range(4):
        serach(x + dx[i], y + dy[i], number)
        
# 5 x 5 크기이므로 브루트포스로 가능한 모든 경우를 탐색
for x in range(5):
    for y in range(5):
        serach(x, y, '')
  
print(len(numbers))

# 시간 복잡도
# 입력: 5x5
# O(25 * 4^5)