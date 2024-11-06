import sys

INT_MAX = sys.maxsize

def solution(sizes):
    max_list = []
    min_list = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            max_list.append(sizes[i][0])
            min_list.append(sizes[i][1])
        else:
            max_list.append(sizes[i][1])
            min_list.append(sizes[i][0])
    return max(max_list)*max(min_list)
            