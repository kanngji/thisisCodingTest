# 특이한 정렬

def solution(numlist, n):
    numlist.sort(reverse=True)
    answer = sorted(numlist, key = lambda x : abs(x-n))
    return answer