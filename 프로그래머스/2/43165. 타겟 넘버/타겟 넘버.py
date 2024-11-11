signs = [1, -1]
ans = 0

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return ans

def dfs(cnt, total, numbers, target):
    global ans
    
    if cnt == len(numbers):
        if total == target:
            ans += 1
        return
    
    for sign in signs:
        dfs(cnt + 1, total + numbers[cnt] * sign, numbers, target)
    return
        