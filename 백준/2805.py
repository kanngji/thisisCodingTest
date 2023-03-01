# 나무자르기
import sys

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
  mid = (start + end) // 2
  trees = 0
  for i in tree:
    trees += i - mid

  if trees >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)


##
import sys

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
  mid = (start + end) // 2
  trees = 0
  for i in tree:
    if i>= mid: # 이부분을 빼먹었꾼...
      trees += i - mid

  if trees >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)
