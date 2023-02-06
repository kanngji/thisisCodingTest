# 팩토리얼 0 의 개수

def fac(num):
  if(num>1):
    return num*fac(num-1)
  else:
    return 1
  
  
  

n=int(input())
a=str(fac(n))
a=a[::-1]
cnt=0
for i in a:
  if i =='0':
    cnt+=1
  else:
    break
print(cnt)