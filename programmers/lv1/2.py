def solution(n):
    flag=False
    answer = -1
    for i in range(1,n+1):
        if i**2== n:
            flag=True
            answer=(i+1)**2
            break
    else:
          return answer 
    return answer