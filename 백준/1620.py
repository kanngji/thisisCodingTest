# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pocketmon = {}
for i in range(1, n + 1):
  mon = input().rstrip()
  pocketmon[i] = mon
  pocketmon[mon] = i

for j in range(m):
  target = input().rstrip() # rstrip()
  if target.isdigit():
    print(pocketmon[int(target)])
  else:
    print(pocketmon[target])


# rstrip() 이란?
# 인자가 없을 경우 오른쪽 공백 제거

