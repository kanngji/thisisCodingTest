# GCD 합

import math

t = int(input())

for i in range(t):
  arr=list(map(int,input().split()))
  hap=0
  for j in range(1,len(arr)-1):
    for k in range(j+1, len(arr)):
      hap+=math.gcd(arr[j],arr[k])
  print(hap)