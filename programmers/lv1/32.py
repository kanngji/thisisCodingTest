# 삼총사

def solution(number):
    res=0
    def dfs(L,hap,cnt):
        
        nonlocal res
        
        if L==len(number):
            if cnt==3 and hap==0:
                res+=1
                return 
                
        else:
            dfs(L+1,hap+number[L],cnt+1)
            dfs(L+1,hap,cnt)
    
    
    dfs(0,0,0)
    answer = res
    return answer