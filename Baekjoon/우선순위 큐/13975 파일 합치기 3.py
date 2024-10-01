import sys, heapq
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    files = list(map(int, read().split()))
    # 파일 목록을 최소 힙으로 변환
    heapq.heapify(files)
    sum = 0
    # 파일이 2개가 남을 때까지
    while (len(files) > 2):
        # 크기가 가장 작은 파일 2개를 합침
        tmp_file = heapq.heappop(files) + heapq.heappop(files)
        sum += tmp_file
        # 합친 임시 파일을 다시 파일 목록에 추가
        heapq.heappush(files, tmp_file)
    print(sum + heapq.heappop(files) + heapq.heappop(files))
    