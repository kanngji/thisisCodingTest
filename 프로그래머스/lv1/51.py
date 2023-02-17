# 카드뭉치

from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1=deque(cards1)
    cards2=deque(cards2)
    goal=deque(goal)
    flag=0
    while True:
        if  len(cards1) >0:
            if  goal[0]==cards1[0]:
                goal.popleft()
                cards1.popleft()
        if len(cards2)>0:
            if goal[0]==cards2[0]:
                goal.popleft()
                cards2.popleft()
        if len(cards1)==0 or len(cards2)==0:
            break
    
    
    print(cards1)
    print(cards2)
    print(goal)
    if len(cards1)>0:
        if cards1[0]!=goal[0]:
            answer="No"
    if len(cards2)>0:
        if cards2[0]!=goal[0]:
            answer="No"
            
    
    
    return answer

########### 다른 사람 풀이 같은 deque로 접근했는데 몇 문제 런차임오류, 틀렷다고 나옴


from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1=deque(cards1)
    cards2=deque(cards2)
    goal=deque(goal)
    
    b,c = cards1.popleft(),cards2.popleft()
    while goal:
        a = goal.popleft()
        if a==b:
            if len(cards1) > 0:
                b=cards1.popleft()
        elif a==c:
            if len(cards2)>0:
                c=cards2.popleft()
        else:
            return "No"
    return "Yes"
    