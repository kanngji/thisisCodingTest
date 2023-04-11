# 나이트의 이동
from collections import deque
import sys

input=sys.stdin.readline
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs(start_x,start_y,goal_x,goal_y):
  q=deque()
  q.append([start_x,start_y])
  s[start_x,start_y]=1
  while q:
    a,b=q.popleft()
    if a == goal_x and b==goal_y:
      print(s[goal_x][goal_y]-1)
    for i in range(8):
      x=a+dx[i]
      y=b+dy[i]
      if 0<= x <n and 0<=y<n and s[x][y]==0:
        q.append([x,y])
        s[x][y]=s[a][b]+1


t=int(input())
for i in range(t):
  n=int(input())
  start_x,start_y=map(int,input().split())
  goal_x,goal_y=map(int,input().split())
  s=[[0]*n for i in range(n)]
  bfs(start_x,start_y,goal_x,goal_y)