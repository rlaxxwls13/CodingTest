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