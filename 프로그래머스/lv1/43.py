# 푸드파이터 대회

from collections import deque

def solution(food):
    answer = ''
    dq = deque()
    
    for i in range(1,len(food)):
        setting=food[i]//2
        for _ in range(setting):
            
            dq.append(i)
    hap=list(dq)
    hap.sort(reverse=True)
    answer=list(dq)+hap
    
    answer.insert(len(answer)//2,0)
    answer=''.join(map(str,answer))
    return answer