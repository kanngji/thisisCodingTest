def solution(n):
    ch=[0]*10001
    answer = []
    d=2
    while d<= n:
        if n%d==0:
            n=n//d
            ch[d]=1
        else:
            d=d+1
    for idx,val in enumerate(ch):
        if val==1:
            answer.append(idx)
        
    return answer

# 파이썬 소인수분해 소스코드 좋다
