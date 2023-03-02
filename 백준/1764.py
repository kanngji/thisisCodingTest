# 듣보잡

n, m = map(int, input().split())
dict1 = {}
cnt = 0
ans = []
for _ in range(n):
  word = input()
  dict1[word] = 1
for _ in range(m):
  word = input()
  if word not in dict1:
    dict1[word] = 1
  else:
    dict1[word] += 1
    cnt += 1

print(cnt)
for key, value in dict1.items():

  if value == 2:

    ans.append(key)

ans.sort()
for i in ans:
  print(i)