T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}")
    n = int(input())
    list = [[0 for j in range(n)] for i in range(n)]
    r, c = 0, 0
    num = 1
    for i in range(n, 0, -1):
        if num == n * n:
            list[r][c] = num
            break

        if (n - i) % 2 == 0:
            # n과 짝수차이일때 : 정방향으로 증가함
            for j in range(i):  # ex) i=4일때 가로로 4만큼, 세로로 3만큼 인덱스를 늘림
                list[r][c] = num
                num += 1
                c += 1
            c -= 1
            r += 1
            for j in range(i - 1):
                list[r][c] = num
                num += 1
                r += 1
            r -= 1
            c -= 1
        else:
            # n과 홀수차이일때 : 역방향으로 증가함
            for j in range(i):
                list[r][c] = num
                num += 1
                c -= 1
            c += 1
            r -= 1
            for j in range(i - 1):
                list[r][c] = num
                num += 1
                r -= 1
            r += 1
            c += 1

    for i in range(n):
        for j in range(n):
            print(list[i][j], end=" ")
        print()

