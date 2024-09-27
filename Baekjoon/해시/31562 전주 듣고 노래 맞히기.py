import sys
read = sys.stdin.readline

N, M = map(int, read().split())

songs = {} # { 노래 제목: 첫 세음 }을 저장할 딕셔너리
for _ in range(N):
    info = read().strip().split()
    songs[info[1]] = ' '.join(info[2:5])

answer = [] # 정답을 저장할 리스트
for _ in range(M):
    find = read().strip()
    count = 0 # 첫 세음이 같은 노래의 개수
    name = ""
    # 딕셔너리를 순회하며 첫 세음이 같은지 카운트
    for s in songs:
        if (find == songs[s]): 
            count += 1
            name = s
    if (count == 1): answer.append(name)
    elif (count == 0): answer.append('!')
    elif (count > 1): answer.append('?')

for a in answer:
    print(a)