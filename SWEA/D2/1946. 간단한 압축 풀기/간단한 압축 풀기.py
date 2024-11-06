T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    str = ""
    for _ in range(n):
        Ci, Ki = input().split()
        str += Ci * int(Ki)
            
    print(f"#{test_case}")
    for i in range(len(str)//10 + 1):
        print(str[:10])
        str = str[10:]
        
        
