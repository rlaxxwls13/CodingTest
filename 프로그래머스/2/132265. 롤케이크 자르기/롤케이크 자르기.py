from collections import Counter

def solution(topping):
    answer = 0
    cs = set()
    yh = Counter(topping)
    
            
    for item in topping:
        cs.add(item)
        yh[item] -= 1
        
        if yh[item] == 0:
            yh.pop(item)
        if len(yh) == len(cs):
            answer += 1
        
    return answer