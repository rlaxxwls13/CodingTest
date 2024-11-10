ans = 0

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]
    choose(dungeons, visited, k, 0)
    return ans
    
def choose(dungeons, visited, k, cnt):
    global ans
    
    ans = max(ans, cnt)
    
    # if 갈수있는던전이없으면 return
    
    # 다음 던전 순회
    for i in range(len(dungeons)):
        if visited[i] == False and k >= dungeons[i][0]:
            visited[i] = True
            choose(dungeons, visited, k - dungeons[i][1], cnt + 1)
            visited[i] = False
    return
    