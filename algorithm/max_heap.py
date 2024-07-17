# 부모가 두 자식값 보다 커야한닫
# 루트값은 항상 최대값 유지
# heap은 최소힙으로 만들어낸다.
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
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)