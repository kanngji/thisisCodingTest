# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1
    arr=[]
    for i in range(1,count+1):
        arr.append(price*i)
    
    if sum(arr)<=money:
        answer= 0
    else:
        answer=sum(arr)-money

    return answer