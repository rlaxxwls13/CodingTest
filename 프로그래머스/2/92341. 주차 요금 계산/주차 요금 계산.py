import math

def solution(fees, records):
    answer = []
    cars_dict = {}
    
    for record in records:
        a = record.split()
        if a[1] in cars_dict:     
            if a[2] == "IN":
                cars_dict[a[1]][0] -= time_to_minutes(a[0])
                cars_dict[a[1]][1] = "IN"
            else:
                cars_dict[a[1]][0] += time_to_minutes(a[0])
                cars_dict[a[1]][1] = "OUT"
        else:
            cars_dict[a[1]] = [(-1) * time_to_minutes(a[0]), "IN"]

    cars_dict = dict(sorted(cars_dict.items()))
    
    for m, inout in cars_dict.values():
        if inout == "IN":
            answer.append(compute_fee(fees, time_to_minutes("23:59") + m))
        else:
            answer.append(compute_fee(fees, m))
        
    return answer

def time_to_minutes(time):
    h , m = time.split(":")
    return int(h) * 60 + int(m)

def compute_fee(fees, m):
    if m <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((m - fees[0])/fees[2]) * fees[3]
    