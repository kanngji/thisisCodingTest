# 숫자 카드 2

import sys
input= sys.stdin.readline

N=int(input())
cards = sorted(list(map(int,input().split())))
M=int(input())
candidate = list(map(int,input().split()))

count = {}

# 해시에 값 추가
for card in cards:
  if card in count: # 해시 count에 값이 있으면 +1
    count[card]+=1
  else:
    count[card]=1 # 해시 count에 값이없으면 추가 (1로 초기화)

for i in range(M):
  a=candidate[i]
  if a in count.keys(): # count key 값에 i를 가지면 출력
    print(count[a], end=' ')
  else:
    print(0, end=' ')