from itertools import permutations

def is_prime(num):
    if num == 0 or num == 1:
        return 0
    if num == 2:
        return 1
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    # 모든 가능한 경우의 수 찾기
    result = 0
    numbers_list = [char for char in numbers]
    all_numbers_list = []
    for i in range(1, len(numbers)+1):
        permu_list = map(lambda x : int(''.join(x)), permutations(numbers_list, i))
        all_numbers_list.extend(permu_list)
    for num in set(all_numbers_list):
        result += is_prime(num)
    return result
