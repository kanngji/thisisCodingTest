# 1,2,3 더하기

import sys
input = sys.stdin.readline

def dfs(num):
    
    if num==1:
        return 1
    elif num==2:
        return 2
    elif num==3:
        return 4
    else:
        arr[num] = dfs(num-1) + dfs(num-2) + dfs(num-3)
        return arr[num]


T = int(sys.stdin.readline())
for _ in range(T):
    target = int(input())
    arr=[0] * (target+1)
    print(dfs((target)))