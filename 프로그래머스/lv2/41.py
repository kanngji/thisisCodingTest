# 리코쳇 최소 몇번이기떄문에 bfs 써야함

from collections import deque

def solution(board):
    answer = 0
    row=len(board)
    col=len(board[0])
    start_x,start_y=0,0
    for i in range(row):
        for j in range(col):
            if board[i][j]=='R':
                start_x,start_y = i,j
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    
    def bfs():
        q=deque()
        q.append((start_x,start_y))
        visited = [[0]*col for _ in range(row)]
        visited[start_x][start_y]=1
        
        while q:
            px,py=q.popleft()
            if board[px][py]=='G':
                return visited[px][py]
            for i in range(4):
                nx,ny=px,py
                while True:
                    nx,ny=nx+dx[i],ny+dy[i]
                    # 장애물 걸릴때
                    if 0<=nx<row and 0<=ny<col and board[nx][ny]=='D':
                        nx-=dx[i]
                        ny-=dy[i]
                        break
                    # 맵 경로 밖으로 갈때
                    if nx<0 or nx>=row or ny<0 or ny>=col:
                        nx-=dx[i]
                        ny-=dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny]=visited[px][py]+1
                    q.append((nx,ny))
        return -1
        
    answer=bfs()
    if answer>0:
        answer-=1
    return answer