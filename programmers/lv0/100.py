# 안전지대

def solution(board):
    answer = 0
    N = len(board)
    # 위험지대
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    
    # 지뢰가 설치된곳
    booms = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1: # 지뢰라면
                booms.append((x,y)) # 지뢰위치 
    
    # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x,y in booms:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx <N and 0<= ny< N: # 맵 밖으로 안튀어나가게
                board[nx][ny]=1
    
    for x in range(N):
        for y in range(N):
            if board[x][y]==0:
                answer+=1
        
    
    return answer