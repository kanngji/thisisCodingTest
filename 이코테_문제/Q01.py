# 모험가 길드
n = int(input())

arr = list(map(int,input().split()))
score=0
people=0
ans=0
for i in range(len(arr)):
  if score < arr[i]:
    score=arr[i]
  people+=1
  
  if people>= score:
    ans+=1
    score=0
    people=0

print(ans)

# 답지 소스코드
n = int(input())
data=list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것 부터 하나씪 확인하며
    count+=1
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+=1 # 총 그룹의 수 증가시키기
        count =0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력