def solution(num, k):
    num=str(num)
    answer = -1
    for idx,val in enumerate(num):
        val=int(val)
        if val == k:
            answer=idx+1
            return answer
    return answer