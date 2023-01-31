# 단지번호 붙이기

# dfs
n = int(input())
graph=[]
num=[]

for i in range(n):
    graph.append(list(map(int,input())))

# 시계방향 
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if graph[x][y]==1:
        global count
        count+=1
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        return True
    return False

count=0
result=0

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            num.append(count)
            result+=1
            count=0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])

# bfs
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(graph,a,b):
    n=len(graph)
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    count=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                count+=1
    return count


n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

cnt=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))