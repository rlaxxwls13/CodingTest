T = 10

def is_palindrome(str):
    new_str = ""
    for i in range(n - 1, -1, -1):
        new_str += str[i]
    return str == new_str


def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    grid = []
    for _ in range(8):
        str = input()
        arr = []
        for char in str:
            arr.append(char)
        grid.append(arr)
    ans = 0
    dxs, dys = [0, 1], [1, 0]
    for x in range(8):
        for y in range(8):
            for dx, dy in zip(dxs, dys):
                str = ""
                for k in range(n):
                    nx, ny = x + k * dx, y + k * dy
                    if not in_range(nx, ny):
                        break
                    str += grid[nx][ny]
                if len(str) == n and is_palindrome(str):
                    ans += 1
    print(f"#{test_case} {ans}")


