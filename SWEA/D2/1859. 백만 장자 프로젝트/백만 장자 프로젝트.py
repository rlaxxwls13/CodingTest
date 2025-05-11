T = int(input())

#최댓값일때 팔아야함
#맨뒤부터 순회하면서 최댓값을 갱신하고 만나는 값이 현재 최댓값보다 작으면 판다, 더 큰 값이면 그 값으로 최댓값을 갱신함
for test_case in range(1, T + 1):
    n = int(input())
    L = list(map(int, input().split()))
    curr_max = L[-1]
    ans = 0
    for i in range(n - 1, -1, -1):
        if L[i] < curr_max:
            ans += curr_max - L[i]
        else:
            curr_max = L[i]
        
    print(f"#{test_case} {ans}")
