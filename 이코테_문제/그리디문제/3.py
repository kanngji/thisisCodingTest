# 문자열 뒤집기
data=input()
c0=0
c1=0

if data[0]=='1':
    c0+=1
else:
    c1+=1

for i in range(len(data)-1):
    if data[i]!=data[i]:
        if data[i+1]=='1':
            c0+=1
        else:
            c1+=1

print(min(c0,c1))