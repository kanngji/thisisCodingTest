# 예산
def solution(d, budget):
    answer = 0
    # 작은애 먼저 하기위해 sort
    d.sort()
    for i in d:
        if budget-i>=0:
            budget-=i
            answer+=1
        
            
    return answer