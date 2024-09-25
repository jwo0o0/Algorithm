import sys
read = sys.stdin.readline 

strings = []
while(1):
    input = read()
    if (input == '.\n'): break
    else: strings.append(input[:-2])

def check_balance(string):
    stack = []
    for s in string:
        # 문자가 괄호인 경우에만 확인
        if (s == '(' or s == ')' or s == '[' or s == ']'):
            # 스택의 길이가 0이거나 여는 괄호인 경우 push
            if (len(stack) == 0 or s == '(' or s == '['):
                stack.append(s)
            # 닫는 괄호인 경우
            else:
                # 마지막 요소와 짝을 이루면 pop
                if ((s == ')' and stack[-1] == '(') or (s == ']' and stack[-1] == '[')):
                    stack.pop()
                # 짝을 이루지 못하면 push
                else:
                    stack.append(s)
        # 문자가 알파벳/공백인 경우 pass
        else:
            continue
    return True if len(stack) == 0 else False

for str in strings:
    print('yes' if check_balance(str) else 'no')