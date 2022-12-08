import sys
sys.setrecursionlimit(10**7)
def fac(n):
    if n==1:
        return 1
    else:
        return n * fac(n-1)

def solution(n):
    answer = 1
    result=0
    while(result<=n):
        result=fac(answer)
        
        dap=answer
        answer+=1
    
    return dap-1