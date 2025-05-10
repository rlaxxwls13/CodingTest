T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

"""
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
    
   """

# 누적합(Prefix Sum)으로 풀기

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(n)]
    ps = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # 누적합 테이블 구하기
    for i in range(1, n+1):
        for j in range(1, n+1):
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + L[i-1][j-1]
    
    ans = -float('inf')
    
    for i in range(1, n - m + 2):
        for j in range(1, n - m + 2):
            sum = ps[i + m - 1][j + m - 1] - ps[i + m - 1][j - 1] - ps[i - 1][j + m - 1] + ps[i - 1][j - 1]
            ans = max(ans, sum)
            
    print(f"#{test_case} {ans}")
