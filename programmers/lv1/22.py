# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt=1
        for j in range(2,i+1):
            if i%j==0:
                cnt+=1
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
    return answer