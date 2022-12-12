from collections import deque

def solution(my_str, n):
    answer = []
    result=''
    dq=deque(my_str)
    while dq:
        for _ in range(n):
            result+=dq.popleft()
            if len(dq)==0:
                break
        
        answer.append(result)
        result=''
    return answer