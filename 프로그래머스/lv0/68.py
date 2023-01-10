def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else: answer+=1
            
            
    return n-answer

# 합성수 찾기 인데 합성수: 약수의 개수가 세 개 이상
# 전체 n의 개수 에서 소수의 개수를 빼면 합성수의 수가 나옴