# 곱하기 혹은 더하기
s="02984"

res = int(s[0])

for i in range(1,len(s)):
  num = int(s[i])
  if num <= 1 or res<=1:
    res+=num
  else:
    res*=num
print(res)