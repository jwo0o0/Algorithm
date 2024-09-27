import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read())

# { 비밀번호 : 개수 }를 저장할 딕셔너리
# value는 0으로 초기화
words = defaultdict(int) 
for _ in range(N):
    word = read().strip()
    # 비밀번호와 뒤집은 비밀번호의 개수에 +1
    words[word] += 1
    words[word[::-1]] += 1

# 딕셔너리를 순회하면서 개수가 2인 비밀번호를 찾음
for word in words:
    if (words[word] == 2):
        print(len(word), word[int(len(word) / 2)])
        break