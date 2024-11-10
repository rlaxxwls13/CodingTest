ans = 0
visited = []

def solution(k, dungeons):
    global visited
    visited = [False for _ in range(len(dungeons))]
    choose(dungeons, k, 0)
    return ans
    
def choose(dungeons, k, cnt):
    global ans
    
    ans = max(ans, cnt)
    
    for i in range(len(dungeons)):
        if visited[i] == False and k >= dungeons[i][0]:
            visited[i] = True
            choose(dungeons, k - dungeons[i][1], cnt + 1)
            visited[i] = False
    return
    