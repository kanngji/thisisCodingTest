def solution(array, n):
    answer = 999
    res=0
    array.sort()
    for i in array:
        minus=abs(n-i)
        if answer>minus:
            res=i
            answer=minus
        
    return res