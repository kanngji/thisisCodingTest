# 평행

from itertools import combinations


def solution(dots):
   
    ok=[]
    combi=list(combinations(dots,2))
    for i,j in combi:
        print(i,j)
        x=abs(i[0]-j[0])
        y=abs(i[1]-j[1])
        print(y/x)
        ok.append(y/x)
    print(ok)
    res=set(ok)
    if len(res)==6:
        return 0
    else:
        return 1
       
    
        
    return answer
# 테케 12번 부터 오류 조합을 써서 각각의 경우의 수의 기울기로 구해서 set해서 중복으로 원소가 사라지면 기울기가 겹치는걸로 
# 판단하는 코드 짯는데 오류 떠서 구글링 해보니 이렇게 짜더라.
# 구글링 코드는 그냥 점 4개에서 2개 지정해서 기울기 구하는 형식
def solution(dots):
    answer = 0
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    if slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    if slope(dots[0],dots[3]) == slope(dots[1],dots[2]):
        answer = 1
    return answer

def slope(dot1,dot2):
    return (dot2[1] - dot1[1] ) / (dot2[0] - dot1[0]) # 기울기 계산 (y축 차이 - x축 차이)