n = int(input())
for _ in range(n):
  s = input()
  cnt = 0
  hap = 0

  for i in s:
    if i == "O":
      cnt += 1

    else:
      cnt = 0
    hap += cnt
  print(hap)