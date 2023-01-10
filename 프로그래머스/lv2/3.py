# 최솟값 만들기

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a,b in zip(A,B):
        pair=a*b
        answer+=pair

    return answer

# zip 함수 쓰기