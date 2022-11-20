# K번째 큰 수
# K번째 큰 수
# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 
# 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
# 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
# 하는 프로그램을 작성하세요.
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
# 은 22입니다.

# 1. 일단 N 과 K 입력받기
n,k = map(int,input().split())

arr=list(map(int,input().split()))
# 2. 중복을 제거하기위해서 set을 쓴다
res=set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            # 넣어서 중복이면 안넣음
            res.add(arr[i]+arr[j]+arr[m])

#sort를 쓰기위해 list로 바꿔준다
res=list(res)
res.sort(reverse=True)
# 하 여기서 3중 for문에서 인자를 k로 줘서 이상한 값 나옴 ㅡㅡ
print(res[k-1])