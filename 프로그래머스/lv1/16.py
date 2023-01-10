# 콜라츠의 추측

def solution(num):
    answer = 0
    cnt=0
    while(True):
        if cnt==500:
            if num!=1:
                answer = -1
                return answer
        if num==1:
            return cnt
        if num%2==0:
            cnt+=1
            num//=2
        else:
            cnt+=1
            num=(num*3)+1
        
        
    