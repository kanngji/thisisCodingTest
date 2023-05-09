# 롤케이크 자르기
from collections import deque
def solution(topping):
    answer = 0
    topping = deque(topping)
    A=[]
    while topping:
        if len(set(A))== len(set(topping)):
            answer+=1
            A.append(topping.popleft())
            
        else:
            A.append(topping.popleft())
            
            
            
    return answer
# TC는 맞았는데 시간초과 
# 다른사람 풀이

from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    answer = 0
    for i in topping:
        dic[i]-=1
        set_dic.add(i)
        
        if dic[i]==0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer+=1
    return answer
