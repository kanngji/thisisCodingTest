# 실패율

from collections import Counter
def solution(스테이지수, 스테이지):
    전체인원 = len(스테이지)
    스테이지에_머물고_있는_사람 = Counter(스테이지)
    answer = {}
    
    for i in range(1,스테이지수+1):
        answer[i] = 0
    
    for i in answer:
        if 스테이지에_머물고_있는_사람[i]!=0 and 전체인원 !=0:
            answer[i] = 스테이지에_머물고_있는_사람[i]/전체인원
        else:
            answer[i]=0
        전체인원 -= 스테이지에_머물고_있는_사람[i]
    
    return sorted(answer, key=lambda x:answer[x], reverse=True)
        
   