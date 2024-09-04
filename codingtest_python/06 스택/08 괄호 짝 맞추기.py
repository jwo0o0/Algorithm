s = "((())()"

def solution(str):
    items = list(str)
    stack = []
    for item in items:
        stack.append(item)
        # 괄호가 상쇄되었는지 검사
        if (len(stack) > 1 and stack[-2] == '(' and stack[-1] == ')'):
            stack.pop()
            stack.pop()
    return len(stack) == 0

print(solution(s))