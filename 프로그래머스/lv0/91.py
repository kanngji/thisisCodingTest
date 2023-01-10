# 직사각형 넓이 구하기

def solution(dots):
    answer = 1
    garo=[]
    sero=[]
    for i in dots:
        garo.append(i[0])
        sero.append(i[1])
    garo.sort()
    sero.sort()
    answer=abs(garo[-1]-garo[0])*abs(sero[-1]-sero[0])
    return answer

# sort를 써야하기 떄문에 set (중복제거는 하지 않았음 )