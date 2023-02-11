# 동전 0

N,K=map(int,input().split())
coins=[]
for _ in range(N):
  coins.append(int(input()))

coins.sort(reverse=True)
cnt=0
i=0
while K!=0:
  cnt+=K//coins[i]
  K=K%coins[i]
  i+=1

print(cnt)
  
  
  
