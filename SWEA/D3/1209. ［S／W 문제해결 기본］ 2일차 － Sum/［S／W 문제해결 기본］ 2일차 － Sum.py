T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_number = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]
    ans = -float('inf')
    left_cross = 0
    right_cross = 0
    for i in range(100):
        width_sum = 0
        height_sum = 0
        for j in range(100):
            width_sum += L[i][j]
            height_sum += L[j][i]
        ans = max({ans, width_sum, height_sum})
        left_cross += L[i][i]
        right_cross += L[99-i][i]
    ans = max({ans, left_cross, right_cross})
    
    print(f"#{test_case} {ans}")
