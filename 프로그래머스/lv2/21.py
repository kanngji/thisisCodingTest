# 귤 고르기

def solution(k, tangerine):
    answer = 0
    # 해시를 생성하자
    a={}
    for i in tangerine:
        if i in a:
            # 사전에 없으면 넣어야지
            a[i]+=1
        else:
            # 서전에 있다면 값을 +1 해야하는데
            a[i]=1
    
    a = dict(sorted(a.items(),key=lambda x: x[1], reverse=True))
    
    for i in a:
        if k<=0:
            return answer
        k-=a[i]
        answer+=1
    return answer
            
            
  # https://velog.io/@minmong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%EA%B7%A4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-Python-velog