def solution(s):
    answer = ''
    ch=[0]*26
    for i in s:
        ch[ord(i)-97]+=1
    for idx,val in enumerate (ch):
        if val==1:
            answer+=chr(idx+97)
        
    return answer