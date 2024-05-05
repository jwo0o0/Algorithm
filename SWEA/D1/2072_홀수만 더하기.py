T = int(input())

numbers = [];
result = [];

for i in range (0, T): 
    numbers = list(map(int, input().split()))
    sum = 0;
    for i in numbers:
        if (i % 2 == 1):
            sum += i
    result.append(sum)
    

for i, sum in enumerate(result):
    print("#{} {}".format(i+1, sum))