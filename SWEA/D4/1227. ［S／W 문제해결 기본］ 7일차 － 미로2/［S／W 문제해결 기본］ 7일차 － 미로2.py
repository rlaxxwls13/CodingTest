from collections import deque

def in_range(x, y):
    return 0 <= x < 100 and 0 <= y < 100
def can_go(x, y):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] != 1
def bfs():
    global possible
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                if grid[nx][ny] == 3:
                    possible = 1
                    return
                q.append((nx, ny))
                visited[nx][ny] = True
                
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = 10
for test_case in range(1, T + 1):
    case_num = int(input())
    grid = []
    for _ in range(100):
        str = input()
        arr = []
        for char in str:
            arr.append(int(char))
        grid.append(arr)
    q = deque()
    visited = [[False for _ in range(100)] for _ in range(100)]
    possible = 0
    
    for i in range(100):
        for j in range(100):
            if grid[i][j] == 2:
                start_x, start_y = i, j
    
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    bfs()
    
    print(f"#{test_case} {possible}")