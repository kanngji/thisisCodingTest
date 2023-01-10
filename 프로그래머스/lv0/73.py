from collections import deque

def solution(numbers, k):
    dq=deque(numbers)
    cnt=0
    ch=1
    answer = 0
    while True:
        cnt+=1
        dq.append(dq.popleft())
        if cnt==2:
            ch+=1
            cnt=0
        if ch==k:
            answer=dq[0]
            break
        
        
        
    return answer