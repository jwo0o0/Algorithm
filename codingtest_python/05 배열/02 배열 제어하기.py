def solution(arr):
    unique_list = list(set(arr))
    unique_list.sort(reverse=True)
    return unique_list

arr = [4, 2, 2, 1, 3, 4]
print(solution(arr))