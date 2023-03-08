# 구간 합 구하기 4

import sys
input=sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(m):
  start, end = map(int, input().split())
  print(sum(arr[start - 1:end]))


# 시간초과
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pfs = list(map(int,input().split()))
for i in range(n-1):
  pfs[i+1]+=pfs[i]

pfs=[0]+pfs

for _ in range(m):
  a,b=map(int,input().split())
  print(pfs[b]-pfs[a-1])

# https://my-coding-notes.tistory.com/212