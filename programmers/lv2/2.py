# jaden case

def solution(s):
    answer = []
    res=[]
    s.lower()
    s=s.split(" ")
    for i in s:
        answer.append(i.capitalize())
    
    answer=' '.join(map(str,answer))
    return answer