import sys
read = sys.stdin.readline

N = int(input())
count = 0

# 스택이 비어있으면 push
# 스택이 비어있지 않으면
#   마지막 요소가 나와 같으면 pop
#   같지 않으면 push
# -> 최종적으로 스택이 길이가 0이면 좋은 단어
def good_word(word):
    stack = []
    for w in word:
        if (len(stack) == 0):
            stack.append(w)
        else:
            if (stack[-1] == w):
                stack.pop()
            else:
                stack.append(w)
    return True if len(stack) == 0 else False
    
for _ in range(N):
    word = read().strip()
    if (good_word(word)):
        count += 1

print(count)