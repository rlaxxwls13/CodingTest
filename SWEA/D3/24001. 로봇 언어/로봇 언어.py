T = int(input())

for test_case in range(1, T + 1):
    str = input()
    dis = 0
    ans = 0
    q = 0
    
    for char in str:
        if char == 'L':
            dis -= 1
            ans = max({ans, abs(dis - q), abs(dis + q)}) 
        elif char == 'R':
            dis += 1
            ans = max({ans, abs(dis - q), abs(dis + q)}) 
        elif char == '?':
            q += 1
            ans = max({ans, abs(dis - q), abs(dis + q)})
 
    print(ans)
            
        
