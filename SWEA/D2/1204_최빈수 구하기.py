T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    cnt = 0 
    maxcnt = 0
    maxnum = numbers[0]
    for j in range(0, len(numbers) - 1):
        cnt += 1
        if (numbers[j] != numbers[j+1]):
            if (cnt >= maxcnt):
                maxnum = numbers[j]
                maxcnt = cnt
            cnt = 0
    print("#{} {}".format(N, maxnum))