# 연속 부분수열의 합 개수

def solution(elements):
    answer = 0
    cycle = elements + elements
    s = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            s.add(sum(cycle[i:i+j]))
    return len(s)