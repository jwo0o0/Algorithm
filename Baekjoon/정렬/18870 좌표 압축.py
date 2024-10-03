import sys
read = sys.stdin.readline

N = int(read())
numbers = list(map(int, read().split()))
sorted_numbers = sorted(numbers)

answers = {} # { X : X를 압축한 결과 }
count = 0 # 지금까지 세어진 숫자의 수 (중복 제외)
for n in sorted_numbers:
    if not n in answers:
        # 아직 세어지지 않았으면 자신보다 작은 숫자를 저장
        answers[n] = count 
        count += 1

for n in numbers:
    print(answers[n], end=' ')