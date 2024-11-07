def solution(brown, yellow):
    answer = []
    #갈색을 나눌 수 있는 각각의 경우에 대해 노란색이 가능인지
    for i in range(3,brown//2):
        h = i
        w = (brown - 2*(i-2)) // 2
        inner_h = h - 2
        inner_w = w - 2
        if inner_h * inner_w == yellow:
            answer.extend([w, h])
            return answer
    
    # 각각 최소 3임
    # 한쪽이 3일때 다른 한쪽은 (brown - 2) // 2 
    # 한쪽이 i일때 다른 한쪽은 (brown - 2*(i-2)) //2
    # 근데 항상 가로가 세로보다 길어야하니까 경우 중에 반은 제외해야됨
    
    return answer