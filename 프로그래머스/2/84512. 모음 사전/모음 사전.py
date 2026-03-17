alpha = ['A', 'E', 'I', 'O', 'U']
words = []

def solution(word):
    dfs('')
    answer = words.index(word)
    return answer

def dfs(curr):
    if len(curr) == 6:
        return
    words.append(curr)
    for i in range(5):
        dfs(curr + alpha[i])
    