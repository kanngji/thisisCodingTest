# 경로 찾기

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 플로이드-워설 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j]=1
# 출력
for row in graph:
    for col in row:
        print(col, end = ' ')
    print()


# BFS
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

def bfs(x): 
    queue=deque()
    queue.append(x)
    check=[0 for _ in range(n)]

    while queue:
        q=queue.popleft()

        for i in range(n):
            if check[i]==0 and graph[q][i]==1:
                check[i]=1
                visited[x][i]=1


for i in range(0,n):
    bfs(i)


