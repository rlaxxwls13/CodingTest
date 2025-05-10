#T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
#for test_case in range(1, T + 1):
n = int(input())
for i in range(1, n+1):
    cnt = 0
    num = i
    for _ in range(4):
        if num % 10 in (3, 6, 9):
            cnt += 1
        num = num // 10
    if not cnt:
        print(i, end=" ")
    else:
        print("-"*cnt, end=" ")
print()
        
