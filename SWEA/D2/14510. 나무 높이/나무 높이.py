def compute_date(day, one, two):
    while True:
        if one <= 0 and two <= 0:
            return day
        day += 1
        # 짝수날
        if day % 2 == 0:
            if two > 0:
            	two -= 1
        # 홀수날
        else:
            if one > 0:
                one -= 1
            elif one <= 0:
                if two > 0:
                    two -= 1
                    one += 1
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    height = list(map(int, input().split()))
    mx_height = max(height)
    diffs = [mx_height - h for h in height]
    one = 0
    two = 0
    
    for diff in diffs:
        one += diff % 2
        two += diff // 2
        
    ans = min(compute_date(0, one, two), compute_date(1, one, two))
    print(f"#{test_case} {ans}")
