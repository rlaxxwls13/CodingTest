def solution(topping):
    answer = 0
    cs = set()
    yh = dict()
    
    for item in topping:
        if item in yh:
            yh[item] += 1
        else:
            yh[item] = 1
            
    for item in topping:
        cs.add(item)
        yh[item] -= 1
        
        if yh[item] == 0:
            del yh[item]
        if len(yh) == len(cs):
            answer += 1
        
    return answer