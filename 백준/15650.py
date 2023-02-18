# N과 M(2)

from itertools import combinations

n,m=map(int,input().split())

for i in combinations([j for j in range(1,n+1)],m):
  print(*i)

# 언패킹 연산자 * 
# 조합 문제
# from itertools import combinations

# 순열 문제
# 뽑는 순서 상관있다.
# from itertools import permutations