def solution(answers):
    """
    n = len(answers)
    
    str1 = "12345"
    str2 = "21232425"
    str3 = "3311224455"
    
    ans1 = str1 * (n//len(str1)) + str1[:n%len(str1)]
    ans2 = str2 * (n//len(str2)) + str2[:n%len(str2)]
    ans3 = str3 * (n//len(str3)) + str3[:n%len(str3)]
    
    count = [0 for _ in range(3)]
    
    for i in range(n):
        if  answers[i] == int(ans1[i]):
            count[0] += 1
        if  answers[i] == int(ans2[i]):
            count[1] += 1
        if  answers[i] == int(ans3[i]):
            count[2] += 1
    
    result = []
    for i in range(3):
        if count[i] == max(count):
            result.append(i+1)
    return result
    """
    n = len(answers)
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    count = [0 for _ in range(3)]
    result = []
    
    for i in range(n):
        for j in range(3):
            if pattern[j][i%len(pattern[j])] == answers[i]:
                count[j] += 1
    
    for i in range(3):
        if count[i] == max(count):
            result.append(i+1)
    return result
       