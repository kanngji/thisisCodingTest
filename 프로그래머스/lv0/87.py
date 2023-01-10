# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    
    for i in range(0,len(num_list),n):
        arr=[]
        for j in range(i,i+n,1):
            arr.append(num_list[j])
        answer.append(arr)
    return answer

# import numpy as np
# def solution(num_list, n):
#     li = np.array(num_list).reshape(-1,n)
#     return li.tolist()