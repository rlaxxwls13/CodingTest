T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        mx_idx = arr.index(max(arr))
        mn_idx = arr.index(min(arr))
        arr[mx_idx] -= 1
        arr[mn_idx] += 1
        
        if max(arr) - min(arr) <= 1:
            break
    print(f"#{test_case} {max(arr) - min(arr)}")
