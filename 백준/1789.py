s = int(input())
hap=0
res=0
for i in range(1,s+1):
  hap+=i
  res+=1
  if hap>s:
    res-=1
    break

print(res)