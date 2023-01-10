def solution(n):
    answer = 2
    for i in range((n//2)+1):
        if i**2 == n:
            answer=1
            
    
    return answer