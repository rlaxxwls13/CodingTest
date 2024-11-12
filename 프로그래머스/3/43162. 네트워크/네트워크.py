visited = []
ans = 0

def solution(n, computers):
    global visited, ans
    
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(i, n, computers)
            ans += 1
    return ans

def dfs(vertex, n, computers):
    for i in range(n):
        if computers[vertex][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i, n, computers)