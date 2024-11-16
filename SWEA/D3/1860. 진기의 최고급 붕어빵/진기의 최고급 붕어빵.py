T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    can_sell = "Possible"
    cnt = 0
    for i in range(0, max(arr) + 1):
        # m초마다 붕어빵을 k개 만듦
        if i != 0 and (i % m) == 0:
            cnt += k
        # 손님이 오면 붕어빵 개수가 하나 줄어듦, 만약 줄어들었는데 음수면 팔지 못한 것
        if i in arr:
            cnt -= 1
            if cnt < 0:
                can_sell = "Impossible"
                break
    print(f"#{test_case} {can_sell}")
                
