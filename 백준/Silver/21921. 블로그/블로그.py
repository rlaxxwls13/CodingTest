n, x = map(int, input().split())
visitors = list(map(int, input().split()))

curr = sum(visitors[:x])
max_visit = curr
cnt = 1

for i in range(1, n-x+1):
    curr = curr - visitors[i-1] + visitors[i+x-1]
    if curr > max_visit:
        max_visit = curr
        cnt = 1
    elif curr == max_visit:
        cnt += 1


if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)
