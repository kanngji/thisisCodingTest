# a->b

def dfs(total,cnt):
  if total>b:
    return 
  if total==b:
    print(cnt)
    exit(0)
    return
  else:
    dfs(total*2,cnt+1)
    dfs(int(str(total)+'1'),cnt+1)
    

a,b=map(int,input().split()) # a,b 입력받기
ans=[]
dfs(a,1)
print(-1)