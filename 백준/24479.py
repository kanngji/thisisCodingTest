# 알고리즘 수업

import sys
sys.setrecursionlimit(10**6) # 재귀 허용 깊이를 수동으로 늘려줌

# 정점의 수 , 간선의 수 , 시작 정점입력 받기
n,m,r = map(int,sys.stdin.readline().split())

# 연결 노드 초기화 (1번 노드와 인덱스 값이 같게 하기 위해 n+1)
graph=[ [] for _ in range(n+1)]
# 방문 순서 그래프 
visited=[0] * (n+1)

# 순차 입력
cnt = 1

def dfs(graph,v,visited):
    global cnt
    # 방문할 때마다 순차 값 변경
    visited[v]= cnt
    # 연결된 노드 방문
    for i in graph[v]:
        # 방문 안한 노드일 경우
        if visited[i]==0:
            # 순차 증가
            cnt+=1
            # dfs 실행
            dfs(graph,i,visited)

# 연결된 노드 입력 받기
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정리
for i in graph(n+1):
    graph[i].sort()

dfs(graph,r,visited)

# 순차 출력
for i in range(n+1):
    if i!=0:
        print(visited[i])

        