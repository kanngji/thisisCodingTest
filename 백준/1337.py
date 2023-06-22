n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort() # 이거 넣으니까 통과되긴하던데
dict1 = {}
for i in range(len(arr)):
  if arr[i] not in dict1:
    dict1[arr[i]] = 1
  for j in range(i + 1, len(arr)):
    if arr[j] - 5 < arr[i]:
      dict1[arr[i]] += 1

dic_max = max(dict1.values())

if dic_max >= 5:
  print(0)
else:
  print(5 - dic_max)

# tc는 다 되는데 왜 틀렸다고 나오지
