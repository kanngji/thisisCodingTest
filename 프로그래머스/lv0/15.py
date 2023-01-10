def solution(n):
    if n==0:
        answer=0
        return answer
    if 0<n<=7:
        answer = 1
        return answer
    if n%7==0:
        answer = n//7
        return answer
    else:
        answer = (n//7)+1
        return answer