T = int(input())
for test_case in range(1, T + 1):
    n, L = map(int, input().split())
    taste, kcal = [0], [0]
    for i in range(n):
        t, k = map(int, input().split())
        taste.append(t)
        kcal.append(k)

    dp = [[-float('inf') for i in range(L + 1)] for _ in range(n+1)]
    
    dp[0][0] = 0
    
    for i in range(1, n+1):
        for j in range(L + 1):
            if j - kcal[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - kcal[i]] + taste[i])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(f"#{test_case} {max(dp[n])}")