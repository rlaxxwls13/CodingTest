T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = [0 for _ in range(n+1)]
    a_idx = 0
    b_idx = 0
    while a_idx < n or b_idx < n:
        while a_idx < n:
            if ans[A[a_idx]] == 0:
                ans[A[a_idx]] = "A"
                break
            a_idx += 1
        while b_idx < n:
            if ans[B[b_idx]] == 0:
                ans[B[b_idx]] = "B"
                break
            b_idx += 1
    for i in range(1, n+1):
        print(ans[i], end="")
    print()
