T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    n = int(input())
    a = list(map(int, input().split()))
    maximum = max(a)
    profit = 0
    for i in range(n-1):
        if(a[i] == maximum):
            maximum = max(a[i+1:n])
            continue
        profit += maximum - a[i]
    print(profit)