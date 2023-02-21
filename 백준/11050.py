# 이항 계수 1

# 이항계수란? 원하는 개수 만큼 순서없이 뽑는 조합

import itertools
N,K = map(int,input().split())

ans=itertools.combinations([i for i in range(1,N+1)],K)
print(len(list(ans)))
