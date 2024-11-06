T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    mx = max(num_list)
    mn = min(num_list)
    new_list = list(filter(lambda x: x!=mx and x!=mn, num_list))
    print(f"#{test_case}", end=" ")
    print(round(sum(new_list)/len(new_list)))
    
