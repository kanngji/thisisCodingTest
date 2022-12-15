def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)

def solution(balls, share):
    answer =fac(balls)//(fac(balls-share)*fac(share))
    return answer

import math

def solution(balls,share):
        return math.comb(balls,share)


#math.comb(n, k)	nCk과 같은 조합 값을 반환한다. (n개의 수에서 k개를 선택)
#math.perm(n, k)	nPk와 같은 순열 값을 반환한다. (n개의 수에서 k를 꺼내 순서대로 나열)