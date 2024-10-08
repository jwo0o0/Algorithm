import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read())

numbers= []
count = defaultdict(int)
for _ in range(N): 
    n = int(read())
    numbers.append(n)
    count[n] += 1
numbers.sort()

# 산술 평균
print(round(sum(numbers) / N))
# 중앙값
print(numbers[N // 2])
# 최빈값
max = max(count.values())
max_nums = []
for num in count:
    if count[num] == max:
        max_nums.append(num)
max_nums.sort()
print(max_nums[1] if len(max_nums) > 1 else max_nums[0])
# 범위
print(numbers[-1] - numbers[0])
