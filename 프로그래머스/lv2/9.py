# 이진변환 반복하기

def solution(s):
    
    
    answer = []
    zerocnt=0
    changecnt=0
    num=0
    while int(s)!=1:
        
        zerocnt+=s.count("0")
        s=s.replace("0",'')
        changecnt+=1
        num=len(s)
        s=bin(num)[2::]
    answer.append(changecnt)
    answer.append(zerocnt)
    return answer