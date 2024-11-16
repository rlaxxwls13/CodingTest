T = int(input())
def dfs(cnt, total):
    if total == k:
        ans.add(tuple(memo))
    if total>k:
        return
    if cnt == n:
        return
    memo.append(cnt)
    dfs(cnt + 1, total + arr[cnt])
    memo.pop()
    dfs(cnt + 1, total)
    
    
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = set()
    memo = []
    dfs(0,0)
    print(f"#{test_case} {len(ans)}")
    
   