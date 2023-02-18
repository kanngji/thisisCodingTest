# 행렬의 곱셈
import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    
    arr_new =arr1@arr2
    answer=arr_new.tolist()
    print(arr_new)
    return answer

# tolist()
#[1 2 3 4 5] => [1,2,3,4,5]

# 다른 사람 풀이

def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer

a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));