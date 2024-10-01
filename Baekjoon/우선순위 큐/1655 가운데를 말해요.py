import sys, heapq
read = sys.stdin.readline

N = int(read())

numbers = []
answer = []
for _ in range(N):
    heapq.heappush(numbers, int(read()))
    print(numbers)
    answer.append(numbers[len(numbers) // 2])
