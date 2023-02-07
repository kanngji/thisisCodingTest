# 이친수

import sys
input=sys.stdin.readline

N = int(input())

DP = [0,1,1]

for i in range(3,91):
    result = DP[i-1] + DP[i-2]
    DP.append(result)

print(DP[N])
