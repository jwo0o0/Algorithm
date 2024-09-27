import sys
read = sys.stdin.readline

L = int(read())
S = read().strip()

INT = [] # 각 문자의 정수값을 저장할 리스트
alphabets = '_abcdefghijklmnopqrstuvwxyz' 
for s in S:
    INT.append(str(alphabets.find(s)))

hash = 0 # 구해야할 해시 값
for i in range(L):
    hash += int(INT[i]) * (31 ** i) # 정수 값 + (31의 자릿수 제곱)

print(hash % 1234567891) # M을 모듈러 연산한 값을 출력