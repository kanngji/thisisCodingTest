# 주식가격

def solution(prices):
    answer = []
    n=len(prices)
    dp=[0]*n
    
    for i in range(n):
        for j in range(i,n-1):
            if prices[i]<=prices[j+1]:
                dp[i]+=1
    return dp
# 한개만 통과하고 나머지 에러 https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec=0
        for q in queue:
            sec+=1
            if price > q:
                break
        answer.append(sec)
    
    return answer