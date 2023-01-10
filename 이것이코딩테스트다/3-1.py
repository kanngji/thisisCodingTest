coins = [500,100,50,10]
n = 1260
cnt=0
for coin in coins:
  cnt+=n//coin
  n=n%coin
print(cnt)

