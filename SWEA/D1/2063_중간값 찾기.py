N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[int(N / 2)])