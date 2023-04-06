# 이중 우선 순위 큐
import heapq
import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    maxheap=[]
    minheap=[]
    n=int(input())
    for _ in range(n):
        cmd=input()
        if cmd[0]=='I':
            heapq.heappush(minheap,int(cmd[2:]))
            heapq.heappush(maxheap,-1*int(cmd[2:]))
        else:
            if len(minheap)==0:
                continue
            if cmd[2]=='-':
                num=heapq.heappop(minheap)
                maxheap.remove(-1*num)
            else:
                num=heapq.heappop(maxheap)
                minheap.remove(-1*num)
    if len(minheap)==0:
        print('EMPTY')
    else:
        print([-1*heapq.heappop(maxheap),heapq.heappop(minheap)])
# 시간 초과
