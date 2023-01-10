# 시져 암호
def solution(s, n):
    answer = ''
    for i in s:
        # 공백은 공백
        if i!= ' ':
            if i >= 'a' and i <= 'z': #소문자일때
            # n만큼 더 가주기
                a=chr(ord(i)+n)
                if ord(a)>122:
                    a=chr(ord(i)+n-26)
                answer+=a
            
            elif i >= 'A' and i <='Z': #대문자일때
            # n만큼 더 가지구
                a=chr(ord(i)+n)
                if ord(a)>90:
                    a=chr(ord(i)+n-26)
                answer+=a
        # 공백일때
        else:
            answer+=' '
        
    return answer