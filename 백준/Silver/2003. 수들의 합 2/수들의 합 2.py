n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
end = 0
curr_sum = 0

for start in range(n):
    while curr_sum < m and end < n:
        curr_sum += a[end]
        end += 1

    if curr_sum == m:
        ans += 1
    
    curr_sum -= a[start]
    

print(ans)
