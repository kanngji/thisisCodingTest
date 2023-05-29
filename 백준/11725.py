# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
tree = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(1,n):
    n1,n2=map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# dfs 탐색함수
def dfs(number):
    visited[number]= True
    for i in tree[number]:
        if not visited[i]:
            answer[i]=number
            dfs(i)

dfs(1) # 부모 노드로부터 dfs 시작

for i in range(2,n+1):
    print(answer[i])
