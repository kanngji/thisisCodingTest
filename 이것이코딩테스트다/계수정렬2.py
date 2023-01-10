n = int(input())

array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# m을 입력받기
m = int(input())

#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))
