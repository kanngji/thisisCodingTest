#k번째 약수
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 
# 작성하시오
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 
# K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.

#1. 일단 두 수 입력받기
n,k=map(int,input().split())
# 약수의 개수 초기화
cnt=0
#2.일단 n의 약수 추려보자
for i in range(1,n+1):
    # 0으로 나누어 떨어지면 약수이다
    if n%i == 0:
        cnt+=1
    # cnt가 1부터 쌓이기때문에 cnt가 k랑 같게 되면 k번째로 작은수가 됨
    if cnt==k:
        # 그렇게 되면 i를 출력하고 반복문 뿌수기
        print(i)
        break
# for else문 for문이 break 없이 다 끝난다면 else문 실행한다
else: 
    print(-1)


# input 8 4 output 8
# input 25 5 output -1
# input 100 5 output 10
# input 100 7 output 25
# input 1000 12 output 125

