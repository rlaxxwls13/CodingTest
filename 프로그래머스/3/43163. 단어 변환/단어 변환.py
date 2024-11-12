ans = 100
visited = []
def solution(begin, target, words):
    global visited, ans
    
    visited = [False for _ in range(len(words))]
    
    dfs(begin, 0, target, words)
    
    if ans == 100:
        ans = 0
    return ans
    

def can_change(curr_word, word):
    diff = 0
    for i in range(len(curr_word)):
        if curr_word[i] != word[i]:
            diff += 1
    return diff == 1


def dfs(curr_word, cnt, target, words):
    global ans
    
    if curr_word == target:
        ans = min(ans, cnt)
    for i in range(len(words)):
        if can_change(curr_word, words[i]) and visited[i] == False:
            visited[i] = True
            dfs(words[i], cnt + 1, target, words)
            visited[i] = False
        