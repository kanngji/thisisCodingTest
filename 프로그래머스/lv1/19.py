# 이상한 문자열
def solution(s):
    answer = ''
    cnt=0
    for i in range(len(s)):
        if s[i]!=' ':
            if cnt==0 or cnt%2==0:
                # 소문자면 대문자로
                if ord(s[i])>=97:
                    answer+=chr(ord(s[i])-32)
                    cnt+=1
                   
                # 대문자면 그냥 대문자
                elif ord(s[i])>=65 and ord(s[i])<=90:
                    answer+=chr(ord(s[i]))
                    cnt+=1
            elif cnt%2==1:
                # 대문자면 소문자로
                if ord(s[i])<=90:
                    answer+=chr(ord(s[i])+32)
                    cnt+=1
                # 솜누자면 그냥 소문자
                elif ord(s[i])>=97 and ord(s[i])<=122:
                    answer+=chr(ord(s[i]))
                    cnt+=1
                
            
        else:
            answer+=' '
            cnt=0
    return answer