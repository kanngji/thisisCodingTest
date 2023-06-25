x = int(input())
cnt = 0
n = 64

while x>0:
    if n>x:
        n=n//2
    else:
        cnt+=1
        x-=n

print(cnt)