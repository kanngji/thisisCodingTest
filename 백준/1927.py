# 최소 힙

import sys
import heapq

input=sys.stdin.readline
n = int(input())
heap=[]

for _ in range(n):
  num = int(input())
  if num!=0:
    heapq.heappush(heap,num)
  else:
    try:
      print(heapq.heappop(heap))
    except:
      print(0)

# 힙 함수 활용하기
# heapq.heappush(heap,item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어있는 경우 indexError가 호출
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함

