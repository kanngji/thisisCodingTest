def solution(arr):
    answer=[]
    for idx,val in enumerate(arr):
        if val==2:
            answer.append(idx)
    
    if answer:
        return arr[answer[0]:answer[-1]+1]
    else:
        return [-1]