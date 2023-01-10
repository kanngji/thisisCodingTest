# 다항식 더하기

def solution(polynomial):
    poly=polynomial.split(" ")
    answer = ''
    xbox=[]
    numbox=[]
    cnt=0
    hap=0
    for i in poly:
        if i=="+":
            continue
        else:
            if 'x' in i:
                xbox.append(i)
            else:
                numbox.append(i)
    
    for i in xbox:
        if len(i)==1:
            cnt+=1
        else:
            cnt+=int(i[:-1:])
    
    
    for i in numbox:
        hap+=int(i)
    
    if hap==0:
        if cnt==1:
            answer="x"
        else:
            answer=str(cnt)+"x"
        
    else:
        if cnt==1:
            answer="x"+" "+"+"+" "+str(hap)
        elif cnt==0:
            answer=str(hap)
        else:
            
            answer=str(cnt)+"x"+" "+"+"+" "+str(hap)
    return answer

# x가 1일때 신경써주고 x가 없을때도 신경써주고
# 상수가 0일때도 신경써주고 다해야함 

