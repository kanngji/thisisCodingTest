# 크기가 작은 부분문자열

def solution(t, p):
    answer = 0
    array=[]
    
    target=len(p)
    for i in range(0,len(t)-target+1):
        string=''
        for j in range(i,target+i):
            string+=t[j]
        array.append(int(string))
    p=int(p)
    for i in array:
        if i<=p:
            answer+=1
    return answer