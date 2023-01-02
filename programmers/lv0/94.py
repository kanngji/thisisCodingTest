# 유한소수 판별하기

def solution(a, b):
    answer = 1
    ch=[0]*(b+1)
    # 약분 해준다
    for i in range(2,a+1):
        if a % i==0 and b%i==0:
            a//=i
            b//=i
        
    # b 소인수 분해
    count=2
    while b!=1:
        if b%count==0:
            b//=count
            ch[count]+=1
        else:
            count+=1
        
    for idx,val in enumerate(ch):
        if idx == 2 or idx==5:
            continue
        elif val!=0:
            answer=2
    
    return answer