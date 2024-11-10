#예를들어 [4,6]을 끊었을때, 4에서 딸려나오는 노드랑 6에서 딸려나오는 노드를 각각 구하면 될듯
#4가 들어있는 전선을 구함, 그 전선에서 4말고 다른 숫자에서 딸려나오는걸 싹다구함

#각 송전탑별로 연결되어있는 탑이 뭐가있는지 리스트를 만듦
#한 전선을 삭제 : 그 전선에 연결된 송전탑의 리스트에서 다른쪽 탑을 삭제함
#두 송전탑에 연결된 송전탑의 차이를 구함

#k번째 송신탑에 연결된 탑 구하는함수

def connected(k, conn_set, wires):
    for wire in wires:
        if k == wire[0] and wire[1] not in conn_set:
            conn_set.update(wire)
            connected(wire[1], conn_set, wires)
        elif k == wire[1] and wire[0] not in conn_set:
            conn_set.update(wire)
            connected(wire[0], conn_set, wires)
    return
    

def solution(n, wires):
    ans = n
    for wire in wires:
        new_wires = wires[:]
        new_wires.remove(wire)
        
        conn_set_a = set([wire[0]])
        conn_set_b = set([wire[1]])
        
        connected(wire[0], conn_set_a, new_wires)
        connected(wire[1], conn_set_b, new_wires)
        
        ans = min(ans, abs(len(conn_set_a) - len(conn_set_b)))
        
    return ans