# 방문길이

def solution(dirs):
    cmd={'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    road = set()
    x,y=(0,0)
    
    for d in dirs:
        
        nx,ny=x+cmd[d][0],y+cmd[d][1]
        print(cmd[d])
        if -5<=nx<=5 and -5<=ny<=5:
            road.add((x,y,nx,ny))
            road.add((nx,ny,x,y))
            x,y=nx,ny
    
    return len(road)//2