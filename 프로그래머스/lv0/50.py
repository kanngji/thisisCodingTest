def solution(array):
    answer = []
    minnum=0
    target_idx=0
    for idx,val in enumerate(array):
        if val>minnum:
            minnum=val
            target_idx=idx
            
    answer.append(minnum)
    answer.append(target_idx)
    return answer