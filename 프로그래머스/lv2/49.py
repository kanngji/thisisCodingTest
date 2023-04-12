# 줄서는 방법

import itertools
def solution(n, k):
    answer=[]
    answer = [i+1  for i in range(n)]
    nPr = list(itertools.permutations(answer,n))
    print(nPr)
    return list(nPr[k-1])
# 시간초과

import math
def solution(n, k):
    answer = []
    people = [i+1 for i in range(n)]
    while n != 0:
        count= math.factorial(n)//n
        a=k// count
        k=k%count
        if k==0:
            answer.append(people.pop(a-1))
        else:
            answer.append(people.pop(a))
        n-=1
    return answer