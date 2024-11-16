T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    p = int(input())
    station = []
    for _ in range(p):
        s = int(input())
        station.append(s)
    cnt = [0 for _ in range(p)]
    for i in range(p):
        for x, y in arr:
            if x <= station[i] <= y:
                cnt[i] += 1
    print(f"#{test_case} ",end="")
    for element in cnt:
        print(element, end=" ")
    print()