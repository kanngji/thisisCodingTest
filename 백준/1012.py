# 유기농 배추

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
  dx=[0,1,0,-1]
  dy=[1,0,-1,0]

  # 시계방향 확인
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if(0<=nx<row) and (0<=ny<col):
      if graph[nx][ny]==1:
        graph[nx][ny]=-1
        dfs(nx,ny)
t=int(input())


for _ in range(t):
  row,col,germ=map(int,input().split())
  graph=[[0]*col for _ in range(row)]
  answer=0
  for _ in range(germ):
    a,b=map(int,input().split())
    graph[a][b]=1

  for i in range(row):
    for j in range(col):
      if graph[i][j] > 0:
        dfs(i,j)
        answer+=1

  print(answer)
      