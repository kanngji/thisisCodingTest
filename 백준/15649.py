from itertools import permutations

n,m=map(int,input().split())

for i in permutations([j for j in range(1,n+1)],m):
  print(*i)

# 언패킹 연산자 * 