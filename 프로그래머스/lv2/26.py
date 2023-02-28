# 점프와 순간이동

def solution(n):
    ans = 0
    while n>0:
        ans+= n%2
        n=n//2

    return ans

# print(1//2) 는 0