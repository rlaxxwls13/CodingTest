T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def square_sum(L, m, x, y):
    sum = 0
    for i in range(m):
        for j in range(m):
            sum += L[x+i][y+j]
    return sum

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(n)]
    ans = -float('inf')
    for x in range(n-m+1):
        for y in range(n-m+1):
            sum = square_sum(L, m, x, y)
            ans = max(ans, sum)
            
    print(f"#{test_case} {ans}")