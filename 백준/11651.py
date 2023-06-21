n = int(input())
arr = []
for _ in range(n):
  s, e = map(int, input().split())
  arr.append([s, e])

arr = sorted(arr, key=lambda x: (x[1], x[0]))
for i in arr:
  print(*i)
