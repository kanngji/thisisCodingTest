# 프린터 큐

from collections import deque

t=int(input())
for _ in range(t):
  answer=0
  n,location=map(int,input().split())
  arr=list(map(int,input().split()))
  d=deque([(v,i) for i,v in enumerate(arr)])

  while len(d):
    item=d.popleft()
    if d and max(d)[0] > item[0]:
      d.append(item)
    else:
      answer+=1
      if item[1]==location:
        break
  print(answer)
  
  
  
