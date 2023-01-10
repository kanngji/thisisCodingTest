# 특정한 수가 한번이라도 등장했는지를 검사하면 되므로 집합 자료형을 이용해서
# 문제해결할수 있다
# set() 함수는 집합자료형을 초기화할 때 사용한다.

n = int(input())

array = set(map(int,input().split()))

m = int(input())

x = list(map(int,input().split()))

for i in x :
    if i in array:
        print('yes',end=' ')
    else:
        print('no', end=' ')

