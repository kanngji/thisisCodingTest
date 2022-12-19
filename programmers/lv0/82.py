from collections import deque

def solution(A, B):
    dqa=deque(A)
    dqb=deque(B)
    answer = 0
    n=len(A)
    # 맨처음 비교를 해야하기 떄문에 x=0
    x=0
    while(True):
        if x==n:
            answer=-1
            break
        if dqa==dqb:
            return answer
        else:
            dqa.appendleft(dqa.pop())
            answer+=1
            x+=1
    return answer