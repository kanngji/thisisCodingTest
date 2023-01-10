# n개의 최소 공배수

import math
def solution(arr):
    answer = 0
    arr.sort()
    while len(arr)!=1:
        answer=arr[-1]
        res=answer*arr[-2]//math.gcd(answer,arr[-2])
        arr.pop()
        arr.pop()
        arr.append(res)
    return res

# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer