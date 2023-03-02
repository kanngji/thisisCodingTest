# 피보나치 함수

import sys
def fibo(num):
  global zero
  global one
  if num==0:
    
    zero+=1
    return 0
  elif num==1:
    one+=1
    return 1
  else:
    return fibo(num-1)+fibo(num-2)

t = int(sys.stdin.readline())

for _ in range(t):
  zero=0
  one=0
  a=int(sys.stdin.readline())
  fibo(a)
  print(zero,one)

## 숏코딩 풀이
T = int(input())
for _ in range(T):
  N=int(input())
  zero,one=1,0 
  for i in range(N):
    zero,one= one,zero+one
  print(zero,one)