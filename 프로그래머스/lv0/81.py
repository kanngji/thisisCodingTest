from collections import deque
def solution(s):
    answer = 0
    dq=deque()
    # 큐를 이용해서 하나씪 다 넣고 z가 나오면 pop?
    
    for i in s.split():
        if i=='Z':
            dq.pop()
        else:
            dq.append(int(i))
    answer=sum(dq)
    return answer