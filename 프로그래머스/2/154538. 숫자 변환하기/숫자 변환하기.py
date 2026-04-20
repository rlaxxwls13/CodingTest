"""
ans_list = []
visited

def solution(x, y, n):
    ans = -1
    dfs(0, x, n, y)
    if ans_list:
        ans = min(ans_list)
    return ans

def dfs(cnt, curr, n, y):
    if curr == y:
        ans_list.append(cnt)
        return
    if curr > y:
        return
    
    dfs(cnt + 1, curr + n, n, y)
    dfs(cnt + 1, curr * 2, n, y)
    dfs(cnt + 1, curr * 3, n, y)
"""


def solution(x, y, n):
    INF = float('inf')
    dp = [INF for _ in range(y+1)]
    dp[x] = 0
    
    for i in range(x, y+1):
        if dp[i] == INF:
            continue
        else:
            if i+n <= y:
                dp[i+n] = min(dp[i+n], dp[i] + 1)
            if i*2 <= y:
                dp[i*2] = min(dp[i*2], dp[i] + 1)
            if i*3 <= y:
                dp[i*3] = min(dp[i*3], dp[i] + 1)
                
    answer = -1 if dp[y] == INF else dp[y]
    return answer