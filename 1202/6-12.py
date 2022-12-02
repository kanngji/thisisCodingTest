n,k=map(int,input().split())

a= list(map(int,input().split()))
b= list(map(int,input().split()))

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교

for i in range(k):
  if a[i]<b[i]:
    # 두 원소를 교체
    a[i],b[i]=b[i],a[i]
  else:
    break

print(sum(a))
