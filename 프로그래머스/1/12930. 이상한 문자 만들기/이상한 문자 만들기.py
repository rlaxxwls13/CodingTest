def solution(s):
    idx = 0
    answer = ''
    for c in s:
        if c == ' ':
            idx = 0
            
        if idx % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()
        
        if c != ' ':
            idx += 1
            
    return answer
    
            
        