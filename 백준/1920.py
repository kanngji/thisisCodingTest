# 수 찾기

N = int(input())

arr1=set(map(int,input().split()))

M = int(input())
arr2=list(map(int,input().split()))

for i in arr2:
  if i in arr1:
    print(1)
  else:
    print(0)

# 이분검색으로
# set 으로 바꾸면 시간초과가 안나는데 왜 안나는지 공부
