from collections import deque
import sys

# input=sys.stdin.readline

n=int(input())
dq=[i for i in range(1,n+1)]
dq=deque(dq)

while len(dq)!=1:
  dq.popleft()
  dq.append(dq.popleft())

print(dq[0])