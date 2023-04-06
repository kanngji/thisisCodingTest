# 이중 우선 순위큐 (강의)
# heapq의 기본은 minheap임

import heapq
def solution(operations):
    answer=[]
    maxheap=[]
    minheap=[]

    for i in operations:
        if i[0]=='I':
            heapq.heappush(minheap,int(i[2:]))
            heapq.heappush(maxheap,-1*int(i[2:]))
        else:
            # i[0]=='D'
            if len(minheap)==0:
                continue
            if i[2]=="-":
                num=heapq.heappop(minheap)
                maxheap.remove(-1*num)

            else:
                num=heapq.heappop(maxheap)
                minheap.remove(-1*num)
    if len(minheap)==0:
        return [0,0]
    else:
        return [-1*heapq.heappop(maxheap),heapq.heappop(minheap)]
