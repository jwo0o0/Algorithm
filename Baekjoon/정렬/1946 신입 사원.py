import sys
read = sys.stdin.readline

T = int(read())
result = []

for _ in range(T): 
    N = int(read())
    # [( 서류 성적, 인터뷰 성적 )] 튜플이 저장된 리스트
    scores = [tuple(map(int, read().split())) for _ in range(N)]
    # 서류 성적을 기준으로 정렬
    scores.sort()
    # 나보다 서류, 인터뷰 모두 높은 지원자가 있으면 탈락
    count = 1 # 최대 인원수
    std = scores[0][1] # 선발되기 위해 넘어야 하는 인터뷰 성적
    for i in range(1, N):
        # 인터뷰 성적을 비교해서 기준보다 높으면 카운트
        # -> 넘어야 하는 기준을 갱신
        if std > scores[i][1]:
            count += 1
            std = scores[i][1]
    result.append(count)
    
for r in result: print(r)