# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**7) # 파이썬 기본 재귀 깊이 제한 풀기
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if visited[i] == False:
            visited[i]=True
            dfs(i)
count = 0

for i in range(1,n+1):
    if visited[i]==False:
        count+=1
        dfs(i)

print(count)