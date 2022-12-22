# 3진법 뒤집기

def solution(n):
    answer = 0
    arr=[]
    while n!=0:
        arr.append(n%3)
        n=n//3
    
    reverse=''.join(map(str,arr[::-1]))
    reverse=reverse[::-1]
    answer=int(reverse,3)
    
    return answer