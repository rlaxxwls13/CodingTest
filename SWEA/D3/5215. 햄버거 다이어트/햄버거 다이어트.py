T = int(input())
def dfs(score, kcal, curr_num):
    global ans
    ans = max(ans, score)
    if curr_num == n:
        return

    if kcal + tk[curr_num][1] <= L:
        dfs(score + tk[curr_num][0], kcal + tk[curr_num][1], curr_num + 1)
    dfs(score, kcal, curr_num + 1)

for test_case in range(1, T + 1):
    n, L = map(int, input().split())
    tk = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")