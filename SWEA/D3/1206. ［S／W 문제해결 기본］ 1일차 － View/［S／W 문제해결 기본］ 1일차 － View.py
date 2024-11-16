#T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(2, n-2):
        #left_1, left_2, right_1, right_2
        left_1 = arr[i] - arr[i-1]
        left_2 = arr[i] - arr[i-2]
        right_1 = arr[i] - arr[i+1]
        right_2 = arr[i] - arr[i+2]
        cnt = min(left_1, left_2, right_1, right_2)
        if cnt > 0:
            ans += cnt
        
    print(f"#{test_case} {ans}")