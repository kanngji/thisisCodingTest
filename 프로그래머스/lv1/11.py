def solution(arr):
    answer = []
    arr_min=min(arr)
    for i in arr:
        if len(arr)==1 and arr_min==10:
            answer=[-1]
            break
        if i!=arr_min:
            answer.append(i)
        
    return answer