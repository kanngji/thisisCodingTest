# set 을 이용해 조건 판별
list1=[]
for _ in range(3):
  list1.append(int(input()))

s1=set(list1)
# 세 각의 크기가 모두 60

if len(s1)==1:
  print("Equilateral")
elif sum(list1)==180 and len(s1)==2:
  print("Isosceles")
elif sum(list1)==180 and len(s1)==3:
  print("Scalene")
elif sum(list1)!=180:
  print("Error")