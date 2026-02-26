import math

def is_prime(n):
    # 소수인지 판별하는 함수
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    ans = 0
    # n을 k진수로 변경
    num = 0
    digit = 1
    while (n > 0):
        num += n % k * digit
        n = n // k
        digit *= 10
    
    curr = 0
    digit = 1
    str_num = str(num)

    candidate = str_num.split('0')
    print(candidate)
    for num in candidate:
        if not num:
            continue
        if is_prime(int(num)):
            ans += 1

    """"
    for i in range(len(str_num) - 1, -1, -1):
        if str_num[i] == '0':
            if is_prime(curr):
                ans += 1
            curr = 0
            digit = 1
            continue
        curr += int(str_num[i]) * digit
        digit *= 10
        
    if is_prime(curr):
        ans += 1
    """
    
    return ans
        