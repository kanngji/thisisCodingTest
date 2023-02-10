# 바이러스
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[ [] for _ in range(n+1)]
visited=[0] * (n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
def dfs(graph,v,visited):
    global cnt
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            cnt+=1
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(cnt)