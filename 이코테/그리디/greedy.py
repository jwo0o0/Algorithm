# 예제 3-1 거스름돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례로 확인
array = [500, 100, 50, 10]

for coin in array: 
    count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전의 개수 
    n %= coin

print(count)