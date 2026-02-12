visited = [False for _ in range(8)]
ans = 0

def solution(k, dungeons):
    dfs(k, dungeons, 0)
    return ans

def dfs(k, dungeons, cnt):
    global ans
    
    ans = max(ans, cnt)
        
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], dungeons, cnt+1)
            visited[i] = False
            
        