from itertools import combinations_with_replacement
from collections import Counter

def solution(n, apeach):
    max_diff = -1
    answer = [-1]
    
    # 점수차를 계산, 점수차가 양수면 라이언, 0 이하이면 어피치 우승
    def calc(apeach, lion):
        a, l = 0, 0
        for k in range(11):
            if apeach[k] == 0 and lion[k] == 0: continue
            elif apeach[k] >= lion[k]: a += (10 - k)
            else: l += (10 - k)
        return l - a
    
    for combi in combinations_with_replacement(range(11), n):
        lion_counter = Counter(combi)
        lion = [lion_counter[i] for i in range(11)]
        diff = calc(apeach, lion)
        if diff <= 0: continue
        # 라이언이 이기고 최대 점수차를 갱신한 경우
        if diff > max_diff:
            max_diff = diff
            answer = lion[:]
        # 낮은 점수를 더 많이 맞힌 경우 우선
        elif diff == max_diff:
            for i in reversed(range(11)):
                if lion[i] > answer[i]:
                    answer = lion[:]
                    break
                elif lion[i] < answer[i]:
                    break
    return answer