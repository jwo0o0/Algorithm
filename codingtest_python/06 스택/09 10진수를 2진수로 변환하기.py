def solution(n):
    result = []
    while (n > 1):
        result.append(str(n % 2))
        n //= 2
    result.append(str(n))
    result.reverse()
    return "".join(result)

print(solution(12345))