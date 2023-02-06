# 접미사 배열

from collections import deque
s=input()
s=deque(s)
answer=[]
while len(s)!=0:
  
  
  a="".join(map(str,s))
  s.popleft()
  answer.append(a)

answer.sort()
for i in answer:
  print(i)