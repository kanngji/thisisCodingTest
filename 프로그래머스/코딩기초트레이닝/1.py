# 두 수의 연산값 비교하기
def solution(a, b):
    answer = 0
    string=str(a)+str(b)
    star=2*a*b
    
    if int(string)>star:
        answer= int(string)
    elif int(string)<star:
        answer=star
    else:
        answer= int(string)
    return answer