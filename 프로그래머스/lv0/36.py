def solution(str1, str2):
    answer = 0
    n=str1.count(str2)
    if n>0:
        answer=1
    else:
        answer=2
    return answer