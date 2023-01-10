# 다음에 올 숫자

def solution(common):
    # flag=1 1이면 등차수열
    # flag=2 2이면 등비수열
    flag=0
    
    if common[1]-common[0]==common[2]-common[1]:
        flag=1
    else:
        flag=2
    if flag==1:
        answer=common[-1]+(common[1]-common[0])
    elif flag==2:
        answer=common[-1]*(common[1]//common[0])
    
    return answer