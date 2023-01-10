import math
def solution(n):
    answer = 0
    gcd=math.gcd(n,6)
    answer=n*6//gcd//6
    return answer