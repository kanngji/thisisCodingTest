# 요세푸스 문제

from collections import deque
n,k=map(int,input().split())
answer=[]
dq=deque()
for i in range(1,n+1):
  dq.append(i)

while dq:
  for i in range(k-1):
    dq.append(dq.popleft())
  answer.append(dq.popleft())
  
answer=', '.join(map(str,answer))
print('<'+answer+'>')