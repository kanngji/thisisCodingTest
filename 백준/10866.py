from collections import deque

# 시간 초과떄문에 import sys

import sys
dq = deque()
n = int(input())

for _ in range(n):
    # t시간 초과 때문에 sys.stdin.readline().split() 하기
  cmd = sys.stdin.readline().split()
  if cmd[0] == 'push_front':
    dq.appendleft(int(cmd[1]))
  elif cmd[0] == 'push_back':
    dq.append(int(cmd[1]))
  elif cmd[0] == 'pop_front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.popleft())
  elif cmd[0] == 'pop_back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.pop())
  elif cmd[0] == 'size':
    print(len(dq))
  elif cmd[0] == 'empty':
    if len(dq) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
  elif cmd[0] == 'back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[-1])
