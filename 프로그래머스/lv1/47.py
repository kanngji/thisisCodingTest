# 과일장수

from collections import deque


def solution(k, m, score):
    score.sort(reverse=True) # 최대 이익을 내기위한 sort()
    answer=0
    score=deque(score)
    
    while len(score)>=m:
        box=[]
        for j in range(m): #  j 반복문안에 popleft() 같이 넣으면 dq score이 깨져서 오류남
            box.append(score[j])
        
        for i in range(m):
            score.popleft()
        
        answer+=box[-1]*len(box)

    return answer