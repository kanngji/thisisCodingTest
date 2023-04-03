# 덧칠하기
from collections import deque
def solution(n, m, section):
    dq=deque()
    
    answer = 0
    for i in section:
        dq.append(i)
    
    arr=list(dq)
    if m==1:
        answer=len(section)
        return answer
    
    for i in arr:
        hap=0
        if m>=hap:
            arr.pop(0)
            answer+=1
            
        else:
            hap+=i
            arr.pop(0)
            
    return answer
# 테케는 다 통과인데 채점은 불합
# 다른 사람은 왤케 쉽게 푸노...

def solution(n, m, section):
    answer = painted = 0
    for each in section:
        if each >= painted:
            painted = each+m
            answer+=1
    return answer