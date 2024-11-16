def arr_to_int(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[len(arr) - 1 - i] * (10 ** i)
    return result


def choose(cnt, arr, n):
    arr_str = ''.join(arr)
    if (arr_str, cnt) in memo:
        return
    memo.add((arr_str, cnt))
    if cnt == n:
        return
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                choose(cnt + 1, arr, n)
                arr[j], arr[i] = arr[i], arr[j]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str, n = input().split()
    n = int(n)
    arr = []
    for char in str:
        arr.append(char)

    memo = set()
    choose(0, arr, n)
    ans = 0
    for num, cnt in memo:
        if cnt == n:
            ans = max(ans, int(num))
    print(f"#{test_case} {ans}")
