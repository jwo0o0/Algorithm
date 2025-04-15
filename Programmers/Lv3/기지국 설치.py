from math import ceil

def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    start = 1
    
    for station in stations:
        left = station - w # 커버 시작
        if start < left:
            gap = left - start
            answer += ceil(gap / coverage)
        start = station + w + 1 # 다음 커버 이후부터 시작
    
    # 마지막 기지국 이후 남은 구간 처리
    if start <= n:
        gap = n - start + 1
        answer += ceil(gap / coverage)
    
    return answer