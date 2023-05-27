# 특정 거리의 도시 찾기

# 슈도 코드
# N(노드개수) M(에지 개수) K(목표 거리) X(시작점)
# A(그래프 데이터 저장 인접 리스트)
# answer (정답리스트)
# visited (방문 거리 저장 리스트)
import sys
from collections import deque
input = sys.stdin.readline
N,M,K,X=map(int,input().split())
A = [[] for _ in range(N+1)]
answer=[]
visited = [-1]*(N+1)

def BFS(v): # BFS 탐색함수 구현
    queue= deque()
    queue.append(v)
    visited[v]+=1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i]==-1:
                visited[i]=visited[now_Node]+1
                queue.append(i)

for _ in range(M):
    S,E = map(int,input().split())
    A[S].append(E)

BFS(X)

for i in range(N+1):
    if visited[i]==K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
