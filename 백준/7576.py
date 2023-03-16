# 토마토

from collections import deque

m,n = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]

# 좌표 넣기
queue=deque([])
#방향 리스트 [dx[0],dy[0]] 은 곧 [-1,0] 이고 이는 왼쪽으로 이동

dx,dy=[-1,1,0,0],[0,0,-1,1] # 왼쪽 오른쪽 아래 위

res=0

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            queue.append([i,j])

# bfs 함수 한번 들어가면 다 돌고 나오니까 재귀 할 필요 x
def bfs():
    while queue:
        # 처음 토마토 좌표 x,y에 꺼내기
        x,y=queue.popleft()
        # 익힐 토마토 찾기
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<= nx<n and 0<=ny<m and matrix[nx][ny]==0:
                matrix[nx][ny]=matrix[x][y]+1
                queue.append([nx,ny])

bfs()
for i in matrix:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res=max(res,max(i))

print(res-1)