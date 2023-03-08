# 비밀번호 찾기

import sys
id_pw={}
n,m = map(int,input().split())
for _ in range(n):
  cmd=input().split()
  id_pw[cmd[0]]=cmd[1]

for _ in range(m):
  target=input()
  print(id_pw[target])