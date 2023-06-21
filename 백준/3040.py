import sys


def dfs(L, sum):
  # 합이 100넘어가면 return
  if sum > 100:
    return
  # L 이 9를 넘어가면 return
  if L > len(arr) - 1:
    return
  if sum == 100:
    for i in range(len(ch)):
      if ch[i] == 1:
        print(arr[i])
    sys.exit(0)
  else:
    ch[L] = 1
    dfs(L + 1, sum + arr[L])
    ch[L] = 0
    dfs(L + 1, sum)


arr = []
for _ in range(9):
  arr.append(int(input()))

sum = 0
ch = [0] * len(arr)
dfs(0, 0)

# 왜 틀렸다고 나오지... tc는 나오는데
