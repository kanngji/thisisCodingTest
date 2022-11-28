def solution(a, b):
    answer = 0
    minn=min(a,b)
    maxn=max(a,b)
    for i in range(minn,maxn+1):
        answer+=i
    return answer