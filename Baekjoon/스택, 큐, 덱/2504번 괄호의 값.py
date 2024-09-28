import sys
read = sys.stdin.readline

string = read().strip()

value_stack = []
sum, tmp = 0, 0

for idx, s in enumerate(string):
    if ((s == '(' or s == '[') and string[idx-1] in ')]'):
        sum += tmp
        tmp = 0    
    if (s == ')' or s == ']'):
        if (s == ')' and string[idx-1] in '(['):
            value_stack.append(2)
        elif (value_stack and s == ')' and string[idx-1] in ')]'):
            tmp += value_stack.pop()
            tmp *= 2
        elif (s == ']' and string[idx-1] in '(['):
            value_stack.append(3)
        elif (value_stack and s == ']' and string[idx-1] in ')]'):
            tmp += value_stack.pop()
            tmp *= 3

sum += tmp     
print(0 if value_stack else sum)