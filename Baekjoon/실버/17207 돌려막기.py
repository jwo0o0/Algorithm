import sys
read = sys.stdin.readline

A = []
B = []
for i in range(5):
    A.append(list(map(int, read().split())))
for i in range(5):
    B.append(list(map(int, read().split())))
    
work = [] # 각자의 일량
for x in range(5):
    sum = 0
    for y in range(5):
        # x번째 사람의 y번째 일량
        for i in range(5):
            sum += A[x][i] * B[i][y]
    work.append(sum)

# 가장 바쁘지 않은 사람 찾기
# work 리스트를 reverse한 후 최솟값의 위치 찾기
# index 메서드는 중복이 있을 경우 앞에 있는 요소를 반환
min = min(work)
work.reverse()
person = ["Youngki", "Jinwoo", "Jungwoo", "Junsuk", "Inseo"]
print(person[work.index(min)])