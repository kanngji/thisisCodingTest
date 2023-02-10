# 요세푸스

from collections import deque
import sys

input=sys.stdin.readline

n,k = map(int,input().split())

dq=[i for i in range(1,n+1)]
dq=deque(dq)
answer=[]
while len(dq)!=0:
  for _ in range(k-1):
    dq.append(dq.popleft())
  answer.append(dq.popleft())

print("<",end='')
print(", ".join(map(str,answer)),end='')
print(">")