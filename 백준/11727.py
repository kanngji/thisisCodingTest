# 2*n 타일링 2

n = int(input())

d = [0] * 1001
d[0] = 1
d[1] = 1
d[2] = 3
d[3] = 5

for i in range(2, n + 1):
  d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n] % 10007)

# for 문에 i 넣어야하는데
# for _ in range(2,n+1):
#   d[n]=d[n-1] 이런식으로 짬...