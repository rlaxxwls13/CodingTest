T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    print(round(sum(map(int, input().split()))/10))
