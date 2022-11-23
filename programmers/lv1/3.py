def solution(s):
    answer = True
    s=s.lower()
    p=s.count('p')
    y=s.count('y')
    if p==0 and y==0:
        return True
    elif p==y:
        return True
    else:
        return False