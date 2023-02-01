# 최소공배수
import math
n = int(input())

for _ in range(n):
    a,b=map(int,input().split())
    answer=a*b//math.gcd(a,b)
    print(answer)