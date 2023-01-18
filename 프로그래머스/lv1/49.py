# 명예의 전당(1)

from heapq import heappop, heappush

def solution(k, score):
    answer = []
    heap = []
    for s in score:
        heappush(heap,s)
        if len(heap) > k:
            heappop(heap)
        answer.append(heap[0])
    return answer

# heap 자료구조
# heap은 완전이진트리 우선순위큐 
# 가장 큰 원소나 가장 작은 숸소를 빠르게 찾는다
# 힙 자료구조는 원소를 삽입또는 삭제하여도 구조를 유지할수 있다.
