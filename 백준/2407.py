# 조합

from itertools import combinations, permutations
import math
n,m = map(int,input().split())

print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))