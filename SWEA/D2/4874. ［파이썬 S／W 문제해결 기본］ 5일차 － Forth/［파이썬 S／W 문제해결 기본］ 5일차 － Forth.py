T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L = list(input().split())
    stack = []
    for x in L:
        if x == '+':
            if len(stack) < 2:
                ans = "error"
                break
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif x == '-':
            if len(stack) < 2:
                ans = "error"
                break
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif x == '*':
            if len(stack) < 2:
                ans = "error"
                break
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif x == '/':
            if len(stack) < 2:
                ans = "error"
                break
            a = stack.pop()
            if a == 0:
                ans = "error"
                break
            b = stack.pop()
            stack.append(b//a)
        elif x == ".":
            if len(stack) == 1:
            	ans = stack.pop()
            else:
                ans = "error"
        else:
            stack.append(int(x))
    
    print(f"#{test_case} {ans}")

    
    
"""
고려해야할점
1. 스택 연산 순서 (ab바뀌면 안됨)
2. 나눗셈 시 // 사용
3. 
"""