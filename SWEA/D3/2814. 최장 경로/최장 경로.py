T = int(input())
ans = 0


def dfs(vertex):
    global curr_len, max_len
    max_len = max(curr_len, max_len)
    for x in range(n + 1):
        if visited[x] == False and x in graph[vertex]:
            curr_len += 1
            visited[x] = True
            dfs(x)
            curr_len -= 1
            visited[x] = False
    return


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = []
    for x in range(n + 1):
        visited = [False for _ in range(n + 1)]
        curr_len, max_len = 1, 0
        visited[x] = True
        dfs(x)
        ans.append(max_len)
    print(f"#{test_case} {max(ans)}")

