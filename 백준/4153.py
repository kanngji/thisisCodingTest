# 직각삼각형

while True:
  a,b,c=map(int,input().split())
  
    
  tri=[a,b,c]
  tri.sort()
  if a==0 and b==0 and c==0:
    break
  
  if (tri[0]**2)+(tri[1]**2)==tri[2]**2:
    print("right")
  else:
    print("wrong")