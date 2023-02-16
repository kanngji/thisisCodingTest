# 문자열 집합

n,m=map(int,input().split())
s=[]


for _ in range(n):
  s.append(input())



s=set(s)
cnt=0

for _ in range(m):
    t= input()
    if t in s:
        cnt+=1

print(cnt)

# set을 이용해서 풀면 시간초과 안나옴