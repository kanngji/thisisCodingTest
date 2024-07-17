import heapq as hq
a = []
while True:
    n = int(input())

    if n == - 1:
        break

    if n == 0 :
        if len(a)==0:
            print(-1)
        else:
            # a에서 자료에서 하나 pop (루트노드 값)
            print(hq.heappop(a))
    else:
        hq.heappush(a,n)
        