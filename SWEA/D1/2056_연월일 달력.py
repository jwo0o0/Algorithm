T = int(input())

dates = []
short = [4, 6, 9, 11]
long = [1, 3, 5, 7, 8, 10, 12]

for i in range (1, T+1):
    dates.append(input())

for i, d in enumerate(dates):
    month = int(d[4:6])
    day = int(d[7:8])
    print("#{}".format(i+1), end=" ")
    if (month < 1 or month > 12):
        print(-1)
        continue
    if (month == 2 and (day < 1 or day > 28)):
        print(-1)
        continue
    if(month in short and (day < 1 or day > 30)):
        print(-1)
        continue
    if(month in long and (day < 1 or day > 31)):
        print(-1)
        continue
    print("{}/{}/{}".format(d[0:4], d[4:6], d[6:8]))
    
 
        