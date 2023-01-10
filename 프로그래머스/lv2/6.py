# 피보나치 수

# def F(n):
#     if n<=1:
#         return n
#     else:
#         return F(n-1)+F(n-2)
    
def F(n):
    _cur,_next=0,1
    for _ in range(n):
        _cur,_next = _next,_cur+_next
    return _cur


def solution(n):
    # 재귀함수 시간 초과 for 문 쓰기
    answer= F(n)%1234567
    
    
    
    return answer