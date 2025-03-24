def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        stack = [i]
        isNetwork = False
        while stack:
            computer = stack.pop()
            for computer, network in enumerate(computers[computer]):
                if network == 1 and not visited[computer]:
                    stack.append(computer)
                    visited[computer] = True
                    isNetwork = True
        if isNetwork: answer += 1
    
    return answer