# 저주의 숫자 3

def solution(n):
    answer = 0
    for _ in range(n):
        answer+=1
        # 3의 배수이거나 3이 들어가 있으면 answer 무한 증가
        while answer %3 ==0 or '3' in str(answer):
            answer+=1
    return answer