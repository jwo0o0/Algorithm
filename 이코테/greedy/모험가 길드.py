# 모험가 길드
n = int(input())
data = list(map(int, input().split()))

data.sort()

# 1 2 2 2 3
# 0 -> 1 -> 3

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
        
print(result)
    