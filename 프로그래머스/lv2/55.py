# 미로탈출

from collections import deque

def bfs(start,end,maps):
    # 탐색방향  시계방향
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    n = len(maps) # 세로
    m = len(maps[0]) #가로
    visited= [[False]*m for _ in range(n)]
    q=deque()
    flag=False
    
    # 초기값 설정
    for i in range(n):
        for j in range(m):
            # 출발하고자 하는 지점이라면 시작점의 좌표
            if maps[i][j]==start:
                q.append((i,j,0))
                visited[i][j]=True
                flag= True
        if flag: break
    while q:
        x,y,cost = q.popleft()
        if maps[x][y] == end:
            return cost
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<= nx <n and 0<= ny <m and maps[nx][ny] !='X':
                if not visited[nx][ny]:
                    q.append((nx,ny,cost+1))
                    visited[nx][ny] = True
    return -1

def solution(maps):
    path1 = bfs('S','L',maps) # 시작지점 => 레버
    path2 = bfs('L','E',maps) # 레버 -> 출구
    
    # 둘다 -1 이 아니라면 탈출
    if path1 != -1 and path2 != -1:
        return path1+path2
    return -1