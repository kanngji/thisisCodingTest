def solution(n):
    n=str(n)
    answer = list(n)
    res=sorted(answer,reverse=True)
    res=''.join(map(str,res))
    res=int(res)
    
    return res