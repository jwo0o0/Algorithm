import sys, heapq
read = sys.stdin.readline 

N = int(read())

# (단어의 길이, 단어) 튜플의 리스트
# heapify를 하면 정렬의 기준: 첫 번째 원소 -> 두 번쨰 원소(사전순)
words = []
for _ in range(N):
    word = read().strip()
    heapq.heappush(words, (len(word), word))

# 중복 제거해서 출력
last = heapq.heappop(words)[1] # 직전에 출력한 단어
print(last)
while words:
    word = heapq.heappop(words)[1]
    # 마지막 원소가 나와 같지 않은 경우에 출력
    if last != word: 
        print(word)
        last = word

