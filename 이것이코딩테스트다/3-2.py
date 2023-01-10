n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data=sorted(data,reverse=True)
first=data[0]
second=data[1]
hap=0
while True:
  for i in range(k): #가장 큰 수를 k번 더하기
    if m==0: # m이 0이라면 반복문 탈출
      break
    hap+=first
    m-=1
  if m==0: # m이 0이라면 반복문 탈출
    break
  hap+=second
  m-=1

print(hap)

  