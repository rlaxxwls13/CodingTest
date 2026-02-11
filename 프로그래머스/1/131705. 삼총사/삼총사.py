from itertools import combinations

def solution(number):
    ans = 0
    for x in combinations(number, 3):
        if sum(x) == 0:
            ans += 1    
    
    return ans