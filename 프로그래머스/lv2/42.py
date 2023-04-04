# 피로도
from itertools import permutations
def solution(k, dungeons):
    dungeons_count = len(dungeons) # 3
    dungeons_list = [i for i in range(dungeons_count)] # [0,1,2]
    for i in range(dungeons_count,0,-1):
        for cases in permutations(dungeons_list,i):
            now = k 
            check= True
            for case in cases:
                if now< dungeons[case][0]:
                    check=False
                    break
                else:
                    now-=dungeons[case][1]
            if check:
                return i
            
# 순열로 모든 경우의 수로 완전탐색한다
# 최개 던전의 수를 return으로 해야하니 i로 
# 처음에 i 3,2,1 이렇게 하고
# [0,1,2]로 순열 탐색하면
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 2)
(2, 0)
(2, 1)
(0,)
(1,)
(2,)
# 이렇게 됨

# 최대 던전수를 알아내야하니 dfs를 써서 풀수도 있음

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer