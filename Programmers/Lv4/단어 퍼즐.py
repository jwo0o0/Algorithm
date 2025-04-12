def solution(strs, t):
    n = len(t)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  

    strs = set(strs)
    max_len = max(len(s) for s in strs)

    for i in range(1, n + 1):
        for l in range(1, max_len + 1):
            if i - l >= 0 and t[i - l:i] in strs:
                dp[i] = min(dp[i], dp[i - l] + 1)

    return dp[n] if dp[n] != float('inf') else -1