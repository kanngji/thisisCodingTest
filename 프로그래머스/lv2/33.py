# 2xn 타일링
def solution(n):
    answer = 0
    d=[0]*60001
    d[1]=1
    d[2]=2
    
    
    for i in range(3,n+1):
        d[i]=(d[i-1]+d[i-2])%1000000007
    return d[i]

# 왜 return d[i]%100000007 말고 위에서 %100000007 하면 시간초과가 안들까?
