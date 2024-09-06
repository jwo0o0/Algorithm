import sys
read = sys.stdin.readline

S = read().strip()

answer = ""
tmp = ""
isTag = False
for s in S:
    if (s == "<"):
        answer += tmp[::-1]
        isTag = True
        tmp = s
    elif (s == ">"):
        answer += tmp + ">"
        tmp = ""
        isTag = False
    elif (s == " "):
        if (isTag): tmp += s 
        else: 
            answer += tmp[::-1] + " "
            tmp = ""
    else:  
        tmp += s
        
answer += tmp[::-1]
print(answer)