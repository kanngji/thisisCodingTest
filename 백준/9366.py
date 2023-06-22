# 삼각형 조건 가장 큰 변이 나머지 두 변의 합 보다 작아야한다
n = int(input())
for i in range(n):
  arr = list(map(int, input().split()))
  arr.sort()

  if arr[0] + arr[1] <= arr[2]:
    print("Case #%s: invalid!" % (i + 1))
  else:
    if len(set(arr)) == 1:
      print("Case #%s: equilateral" % (i + 1))

    elif len(set(arr)) == 2:
      print("Case #%s: isosceles" % (i + 1))

    else:
      print("Case #%s: scalene" % (i + 1))
